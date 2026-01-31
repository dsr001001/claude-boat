# Claude Boat - Creative Projects

A collection of creative tools: an animated motorboat SVG and an interactive collaborative poem writer.

## Projects Included

### 1. Motorboat Animation
A pure HTML/CSS/SVG animation featuring a motorboat sailing across an animated seascape.

**Features:**
- Fully self-contained single HTML file
- No dependencies, no build process
- Smooth CSS3 animations with GPU acceleration
- Responsive design (works on desktop, tablet, mobile)
- Accessible (respects `prefers-reduced-motion`)

**File:** `boat-animation.html`

**How to use:**
- Double-click `boat-animation.html` to open in your browser
- Animation loops continuously
- View detailed documentation in `README.md`

**What's included:**
- Boat with hull, cabin, windows, motor, propeller, and flag
- Animated water waves with undulation
- Splash and foam effects
- Synchronized multi-layer animations

---

### 2. Collaborative Poem Writer CLI
An interactive Python CLI script for creating poems in real-time with Claude Code as your AI collaborator.

**Features:**
- Live interactive experience (no file editing between turns)
- Real-time display of the developing poem
- Preview mode before adding each line
- Session-based storage with timestamped files
- Clear separation of user vs. agent lines

**File:** `poem_cli.py`

**How to use:**
1. Update `claude_location.txt` with your Claude Code executable path
2. Run: `python poem_cli.py`
3. Type your poem lines, preview them, and confirm
4. Claude Code generates the next line automatically
5. Type `<EOF>` when done
6. Poem saves to `poems/` directory

**Setup:**
- Python 3.7+ required
- Claude Code must be installed
- See `POEM-CLI-USAGE.md` for detailed instructions

**How it works:**
- Agent writes line 1 (opening)
- You write line 2
- Agent writes line 3
- Continue alternating until complete
- Agent adds final closing line

**Example flow:**
```
AGENT:  The harbor keeps its secrets in the fog.
USER:   Where ships arrive but never quite return.
AGENT:  The lighthouse beam cuts through the darkening haze.
USER:   A guardian watching over restless souls.
...
```

---

## Directory Structure

```
claude-boat/
├── README_OVERALL.md           # This file
├── README.md                   # Motorboat animation docs
├── README-POEM.md              # Poem agent documentation
├── POEM-CLI-USAGE.md           # Poem CLI setup & usage
│
├── boat-animation.html         # Motorboat SVG animation
│
├── poem_cli.py                 # Poem writer CLI script
├── poem_cli_requirements.txt   # Dependencies (none needed)
├── claude_location.txt         # Claude Code executable path
│
├── poems/                      # Generated poems (auto-created)
│   ├── poem_2026-01-31_14-32-45.txt
│   ├── poem_2026-01-31_15-10-23.txt
│   └── ...
│
└── .gitignore                  # Git ignore rules
```

---

## Quick Start

### Animation (2 seconds)
1. Open `boat-animation.html` in your browser
2. Watch the motorboat sail across the screen

### Poem Writer (5 minutes setup)
1. Find where Claude Code is installed
2. Edit `claude_location.txt` with the full path
3. Run: `python poem_cli.py`
4. Follow the prompts to create your poem

---

## Technologies Used

### Motorboat Animation
- **HTML5** - Semantic structure
- **CSS3** - Keyframe animations, gradients, transforms
- **SVG** - Vector graphics with bezier curves
- **GPU Acceleration** - Hardware-optimized animations

### Poem Writer
- **Python 3** - Core script logic
- **Subprocess** - Communication with Claude Code
- **File I/O** - Poem persistence

---

## Features Comparison

| Feature | Motorboat | Poem CLI |
|---------|-----------|----------|
| Interactive | No (watch only) | Yes (collaborate) |
| Customizable | Colors, speed, complexity | Theme, length, style |
| Dependencies | None | Claude Code required |
| Output | Visual animation | Text poems |
| Time to create | Instant | 5-10 minutes per poem |
| Shareable | HTML file | Text files |

---

## Use Cases

### Motorboat Animation
- Portfolio demonstrations
- Website backgrounds or embedded visualizations
- Educational material about CSS animations
- Presentations and marketing materials
- Creative inspiration (watching motion)

### Poem Writer
- Creative writing practice
- Poetry collaboration exercises
- Exploring AI-human creative partnerships
- Daily poetry prompts
- Content generation for projects
- Learning poetic techniques

---

## Documentation

**For Motorboat Animation:**
- `README.md` - Complete technical documentation
  - Architecture overview
  - Detailed animation descriptions
  - Performance optimization
  - Browser compatibility
  - Customization guide

**For Poem Writer:**
- `README-POEM.md` - Agent description and workflow
- `POEM-CLI-USAGE.md` - Setup, usage, and troubleshooting

---

## Requirements

### Motorboat Animation
- Any modern web browser (Chrome, Firefox, Safari, Edge, Opera)
- No internet required
- Works on desktop, tablet, mobile

### Poem Writer
- Python 3.7 or higher
- Claude Code installed (see setup instructions)
- No API key needed (uses local Claude Code)

---

## Tips

### For Animation
- Modify colors in the SVG `<defs>` section
- Adjust animation speed by changing CSS duration values
- Customize boat size with transform scale
- Responsive design works at any screen size

### For Poem Writer
- Match the agent's rhythm and meter for cohesion
- Let themes emerge naturally
- Don't overthink—spontaneous lines work best
- You have unlimited time between turns
- Type `n` to retry if you make a typo

---

## Troubleshooting

### Animation doesn't display
- Update your browser (needs modern CSS/SVG support)
- Check browser console for errors
- Try a different browser

### Poem CLI won't run
- Verify Claude Code path in `claude_location.txt`
- Ensure Python 3 is installed
- Check that Claude Code executable exists at the specified path
- Run Claude Code manually to verify it works

### Poems aren't saving
- Check that you have write permissions in the directory
- Verify `poems/` directory exists (auto-created)
- Try saving to a different location if path is too long

---

## About the Project

This is a collection of creative tools built with Claude Code. Both projects demonstrate:
- Creative use of web technologies (animation)
- Human-AI collaboration patterns (poetry)
- Zero-dependency, self-contained implementations
- Interactive and engaging user experiences

**Created:** 2026
**License:** Free to use and modify

---

## Getting Help

- Check the specific README files for each project
- Review POEM-CLI-USAGE.md for common issues
- Examine the HTML source for animation details
- Read the Python script comments for CLI logic

Enjoy creating!
