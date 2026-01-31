# Collaborative Poem Writer Agent

An interactive agent that collaboratively writes poetry with users, alternating between AI-generated lines and user contributions.

## Overview

The Collaborative Poem Writer is a specialized agent available within Claude Code that enables real-time creative collaboration on poetry. The agent writes odd-numbered lines while you contribute even-numbered lines, creating a seamless back-and-forth creative process that produces cohesive, meaningful poems.

## How It Works

1. **Initialization**: Launch the collaborative poem writer agent
2. **First Line**: The agent writes line 1 and saves it to `poem.txt`
3. **Monitoring**: The agent monitors `poem.txt` every 10 seconds for your input
4. **Alternation**: You add the next line (line 2), the agent adds line 3, continuing back-and-forth
5. **Completion**: Write `<EOF>` on a new line to signal the end of the poem
6. **Finale**: The agent adds a final closing line and completes the poem

## Usage

### Via Claude Code CLI

```bash
/agents
# Create or select the collaborative-poem-writer agent

# Then ask:
ask collaborative poem writer to start the poem
```

### Programmatic Usage

Use the Task tool with the `collaborative-poem-writer` subagent type:

```
Task Parameters:
- subagent_type: "collaborative-poem-writer"
- description: "Start collaborative poem writing"
- prompt: "Start a collaborative poem. Write the first line and save it to poem.txt. Monitor for user input every 10 seconds. Continue alternating lines until the user writes '<EOF>'."
```

## File Format

The poem is stored in a file named `poem.txt` with the following structure:

- **Odd-numbered lines** (1, 3, 5, ...): Written by the agent
- **Even-numbered lines** (2, 4, 6, ...): Written by the user
- **Final line**: Added by the agent after `<EOF>` is detected

Example output:
```
Whispers drift through morning mist,
winds through the woodland swift,
Carrying secrets, ancient and old,
Some happy and warm, some dry and cold,
They swirl and dance through fading light,
showing e'ryone their power and might,
Until the stars emerge so bright and true,
showing the way to ships and 'er crew,
Through endless seas they venture forth,
Hopeful and brave, going, south and north,
Yet still the whispers call them home,
"This is yours - the brown earth and the blue dome"
And so they rest, their journey complete at last.
```

## Process Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. User launches collaborative-poem-writer agent            │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Agent writes line 1 and saves to poem.txt                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Agent monitors poem.txt every 10 seconds                 │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌──────────────────┐    ┌──────────────────────┐
│ User adds line 2 │    │ No input detected    │
└────────┬─────────┘    └──────────┬───────────┘
         │                         │
         ▼                         ▼
┌──────────────────┐    ┌──────────────────────┐
│ Agent adds line 3│    │ Wait 10 seconds      │
└────────┬─────────┘    └──────────┬───────────┘
         │                         │
         └────────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │ Continue alternating  │
            │ until user writes     │
            │ '<EOF>'               │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ Agent adds final     │
            │ closing line         │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │ poem.txt complete!   │
            └──────────────────────┘
```

## Tips for Best Results

- **Rhythm & Meter**: Try to match the agent's line length and rhythm pattern for better cohesion
- **Thematic Consistency**: Let themes emerge naturally through the alternation—don't force new directions
- **Emotional Arc**: Use your lines to deepen or shift the emotional tone
- **Timing**: Complete your line before the 10-second monitoring interval expires
- **Spontaneity**: Don't overthink—spontaneous, creative contributions often produce the most interesting poems

## Technical Details

- **Monitoring Interval**: 10 seconds between file checks
- **Output File**: `poem.txt` (in the current working directory)
- **Completion Signal**: `<EOF>` on a new line triggers poem completion
- **Agent Type**: Specialized collaborative-poem-writer with file I/O and timing capabilities
- **Agent ID**: Can be resumed using the agent ID returned after execution

## Example Session

### Starting the Agent
```
$ ask collaborative poem writer to start the poem
```

### Agent Writes Line 1
Agent creates `poem.txt` with:
```
Whispers drift through morning mist,
```

### User Writes Line 2
User opens `poem.txt` and adds:
```
Whispers drift through morning mist,
winds through the woodland swift,
```

### Agent Writes Line 3
Agent detects new input and adds:
```
Whispers drift through morning mist,
winds through the woodland swift,
Carrying secrets, ancient and old,
```

### Continue...
Process repeats until user writes `<EOF>` to complete.

## Integration with Claude Code

The Collaborative Poem Writer agent integrates seamlessly with Claude Code's agent system:

- **No External Dependencies**: Uses only file I/O and standard timing
- **Transparent Workflow**: User can monitor progress by viewing `poem.txt` at any time
- **Pauseable**: If the user doesn't respond within a reasonable time, the agent waits indefinitely
- **Resumable**: If interrupted, the agent ID can be used to resume from the current state

## Creative Applications

The Collaborative Poem Writer can be used for:

- **Educational Poetry Writing**: Learn poetic techniques through collaborative creation
- **Creative Exercises**: Daily poetry prompts and collaborative challenges
- **Content Generation**: Rapid prototyping of poetic content for projects
- **Creative Partnerships**: Experience how different "voices" (AI + human) create unexpected combinations
- **Therapeutic Writing**: Guided reflection through alternating contributions
