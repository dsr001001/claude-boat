#!/usr/bin/env python3
"""
Interactive Collaborative Poem Writer CLI
Create poems in real-time with alternating user and AI lines using Claude Code.
Each session saves to a separate timestamped file.
"""

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

# Create poems directory if it doesn't exist
POEMS_DIR = Path(__file__).parent / "poems"
POEMS_DIR.mkdir(exist_ok=True)

# Read Claude Code location from file
SCRIPT_DIR = Path(__file__).parent
CLAUDE_LOCATION_FILE = SCRIPT_DIR / "claude_location.txt"

def get_claude_executable() -> str:
    """Read Claude Code executable path from claude_location.txt"""
    if not CLAUDE_LOCATION_FILE.exists():
        print(f"Error: {CLAUDE_LOCATION_FILE.name} not found.")
        print("Please create a file named 'claude_location.txt' with the full path to Claude Code executable.")
        sys.exit(1)

    with open(CLAUDE_LOCATION_FILE, "r") as f:
        path = f.read().strip()

    if not path or path.startswith("C:\\path\\to"):
        print(f"Error: {CLAUDE_LOCATION_FILE.name} contains placeholder path.")
        print("Please edit it with the actual path to your Claude Code executable.")
        sys.exit(1)

    if not Path(path).exists():
        print(f"Error: Claude Code executable not found at: {path}")
        print(f"Please verify the path in {CLAUDE_LOCATION_FILE.name}")
        sys.exit(1)

    return path

CLAUDE_EXECUTABLE = get_claude_executable()


def format_poem_display(lines: list[dict]) -> str:
    """Format the poem with clear separation between user and agent lines."""
    if not lines:
        return ""

    display = "\n"
    for i, line_data in enumerate(lines, 1):
        source = "USER" if line_data["source"] == "user" else "AGENT"
        display += f"{source}:  {line_data['text']}\n"

    return display


def get_agent_line(poem_so_far: str, is_opening: bool = False) -> str:
    """Get the next line from Claude Code via subprocess."""
    if is_opening:
        prompt = "Write the first line of an original poem. Respond with only the line itself, nothing else."
    else:
        prompt = f"""You are a creative poetry collaborator. Continue this poem with the next line.

Current poem:
{poem_so_far}

Respond with ONLY the next line of poetry. Do not include explanations, line numbers, or meta-commentary. Just the poetic line itself."""

    try:
        result = subprocess.run(
            [CLAUDE_EXECUTABLE, "-p", prompt],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Error from Claude Code: {result.stderr}")
            return "(Claude Code error - please try again)"
    except subprocess.TimeoutExpired:
        print("Error: Claude Code took too long to respond.")
        return "(Timeout - please try again)"
    except Exception as e:
        print(f"Error calling Claude Code: {e}")
        return "(Error - please try again)"


def get_poem_text(lines: list[dict]) -> str:
    """Convert lines list to poem text for passing to Claude Code."""
    return "\n".join([line["text"] for line in lines])


def main():
    """Main CLI loop for collaborative poem writing."""
    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    poem_file = POEMS_DIR / f"poem_{timestamp}.txt"

    print("\n" + "=" * 60)
    print("COLLABORATIVE POEM WRITER")
    print("=" * 60)
    print(f"Session: {timestamp}")
    print(f"Saving to: {poem_file.name}")
    print("\nType your lines. Type <EOF> on its own line to finish.")
    print("=" * 60)

    lines = []

    # Agent starts with first line
    print("\nGenerating opening line...\n")
    agent_first_line = get_agent_line("", is_opening=True)
    lines.append({"source": "agent", "text": agent_first_line})

    print(format_poem_display(lines))

    # Main alternating loop
    while True:
        try:
            # Get user input
            user_input = input("\nYour line: ").strip()

            if user_input.upper() == "<EOF>":
                print("\n" + "=" * 60)
                print("Adding final line...")
                print("=" * 60)

                # Get agent's final line
                poem_so_far = get_poem_text(lines)
                final_prompt = f"""You are a creative poetry collaborator. Write one final closing line to conclude this poem.

Current poem:
{poem_so_far}

Respond with ONLY the final line of poetry. Do not include explanations or meta-commentary."""

                try:
                    result = subprocess.run(
                        [CLAUDE_EXECUTABLE, "-p", final_prompt],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    if result.returncode == 0:
                        final_line = result.stdout.strip()
                    else:
                        final_line = "(Unable to generate final line)"
                except Exception as e:
                    final_line = "(Error generating final line)"

                lines.append({"source": "agent", "text": final_line})

                # Save complete poem
                with open(poem_file, "w") as f:
                    for line_data in lines:
                        f.write(f"{line_data['text']}\n")

                print(format_poem_display(lines))
                print("\n" + "=" * 60)
                print(f"POEM COMPLETE!")
                print(f"Saved to: {poem_file.name}")
                print(f"Total lines: {len(lines)}")
                print("=" * 60 + "\n")
                break

            if not user_input:
                print("(empty line, skipping)")
                continue

            # Preview mode
            print(f"\nPreview: {user_input}")
            confirm = input("Confirm? (y/n): ").strip().lower()

            if confirm != "y":
                print("Skipped.")
                continue

            # Add user line
            lines.append({"source": "user", "text": user_input})

            # Get agent response
            print("\nGenerating next line...")
            poem_so_far = get_poem_text(lines)
            agent_line = get_agent_line(poem_so_far)
            lines.append({"source": "agent", "text": agent_line})

            # Display updated poem
            print(format_poem_display(lines))

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Saving current poem...")
            with open(poem_file, "w") as f:
                for line_data in lines:
                    f.write(f"{line_data['text']}\n")
            print(f"Saved to: {poem_file.name}")
            sys.exit(0)
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
