# Poem CLI - Interactive Collaborative Poetry Writer

A standalone Python CLI script for creating poems in real-time with Claude via Claude Code. Each session creates a separate timestamped poem file.

## Setup

### 1. Install Claude Code
Install Claude Code from: https://github.com/anthropics/claude-code

### 2. Configure Claude Location
Since Claude Code might not be in your PATH, create a `claude_location.txt` file in the same directory as `poem_cli.py`:

```
C:\full\path\to\claude-code.exe
```

Or on macOS/Linux:
```
/usr/local/bin/claude-code
```

Replace with the actual full path to your Claude Code executable.

### 3. No Additional Dependencies
The script uses only Python's standard library. No pip packages needed!

## Usage

### Run the Script
```bash
python poem_cli.py
```

### Interactive Session Flow

1. **Session Starts**: Shows timestamp and poem filename
2. **Agent Writes Opening Line**: Generates the first line
3. **You Write a Line**: Type your contribution and press Enter
4. **Preview & Confirm**: See what you typed, confirm with `y` to proceed
5. **Agent Responds**: Generates the next line automatically
6. **Poem Displays**: Full poem shown with USER/AGENT labels
7. **Repeat**: Continue alternating until done
8. **Finish**: Type `<EOF>` on its own line
9. **Save**: Poem automatically saved to `poems/` directory

### Example Session

```
============================================================
COLLABORATIVE POEM WRITER
============================================================
Session: 2026-01-31_14-32-45
Saving to: poem_2026-01-31_14-32-45.txt

Generating opening line...

AGENT:  Whispers drift through morning mist,

Your line: winds through the woodland swift,

Preview: winds through the woodland swift,
Confirm? (y/n): y

Generating next line...

USER:  winds through the woodland swift,
AGENT:  Carrying secrets, ancient and old,

Your line: Some happy and warm, some dry and cold,
...
```

## Features

- **Live Interactive Editing**: No more opening/closing text editors
- **Preview Mode**: See your line before it's added to the poem
- **Clear Separation**: User and Agent lines are clearly labeled
- **Real-time Display**: Poem updates after each turn
- **Session Tracking**: Timestamped filenames for easy reference
- **Auto-save**: Poems saved automatically on completion
- **Graceful Exit**: Ctrl+C saves your work and exits

## File Organization

All poems are saved in a `poems/` directory alongside the script:
```
claude_boat/
├── poem_cli.py
├── poem_cli_requirements.txt
└── poems/
    ├── poem_2026-01-31_14-32-45.txt
    ├── poem_2026-01-31_15-10-23.txt
    └── poem_2026-02-01_09-45-12.txt
```

## Tips

- **Rhythm Matching**: Try to match the length and meter of previous lines
- **Build on Theme**: Let the theme emerge naturally through conversation
- **Quick Typing**: You have unlimited time—no timeout between turns
- **Typos**: If you make a mistake, just type `n` at the confirm prompt and try again
- **Inspiration**: Don't overthink it—spontaneous lines often work best

## Troubleshooting

### "claude_location.txt not found"
Create a `claude_location.txt` file in the same directory as `poem_cli.py` with the full path to Claude Code.

### "Claude Code executable not found at: ..."
The path in `claude_location.txt` is incorrect. Verify the actual location of your Claude Code executable and update the file.

### Claude Code takes too long to respond
The script has a 30-second timeout. If Claude Code is slow:
- Try running Claude Code directly first to ensure it's working
- Check your system resources (CPU, memory)
- Claude Code might still be initializing on first run

### Poem file not saving
The script automatically creates a `poems/` directory. If saving fails:
- Check that you have write permissions in the directory
- Ensure the path isn't too long (Windows has PATH length limits)

### Empty or garbled responses from Claude Code
Claude Code might be returning extra text beyond just the poem line:
- Try running Claude Code directly with a test prompt
- Check the Claude Code version is up to date

## Notes

- Each poem is independent; start a new session for a new poem
- Poems are plain text files—easy to read, edit, or share
- Responses come from your local Claude Code installation
- All processing happens locally—no external API calls
