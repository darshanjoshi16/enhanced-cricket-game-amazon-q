# Project Structure

```
enhanced-retro-cricket/
├── 📁 src/                          # Source code directory
│   ├── 🐍 enhanced_cricket.py       # Main game engine
│   ├── 🔊 sound_effects.py          # Audio generation system
│   └── 📸 screenshot_generator.py   # Demo screenshot generator
│
├── 📁 screenshots/                  # Demo screenshots
│   ├── 📷 main_menu.png            # Main menu interface
│   ├── 📷 gameplay.png             # Active gameplay
│   ├── 📷 boundary_celebration.png # Boundary celebration
│   ├── 📷 milestone_celebration.png# Milestone achievement
│   ├── 📷 game_over.png            # Game over screen
│   └── 📝 README.md                # Screenshot documentation
│
├── 📁 docs/                        # Documentation
│   └── 📋 TECH_STACK.md            # Technology stack details
│
├── 📁 assets/                      # Game assets (future use)
│   └── (placeholder for sprites, sounds, etc.)
│
├── 🐍 run_game.py                  # Cross-platform game launcher
├── 🐧 run_game.sh                  # Linux/macOS launcher script
├── 🪟 run_game.bat                 # Windows launcher script
│
├── 📋 requirements.txt             # Python dependencies
├── ⚙️ setup.py                     # Package setup configuration
├── 📄 LICENSE                      # MIT license
├── 🚫 .gitignore                   # Git ignore rules
│
├── 📖 README.md                    # Main project documentation
├── 🔧 INSTALL.md                   # Installation guide
├── 📊 PROJECT_STRUCTURE.md         # This file
└── 💬 CONVERSATION_PROMPTS.txt     # Complete development session prompts
```

## 📁 Directory Descriptions

### `/src/` - Source Code
Contains all Python source files for the game:
- **enhanced_cricket.py**: Main game engine with all classes and game logic
- **sound_effects.py**: Procedural audio generation system
- **screenshot_generator.py**: Utility for capturing demo screenshots

### `/screenshots/` - Demo Materials
Visual documentation of the game:
- High-quality PNG screenshots of different game states
- README with descriptions of each screenshot
- Perfect for GitHub repository showcase

### `/docs/` - Documentation
Technical documentation:
- **TECH_STACK.md**: Comprehensive technology stack overview
- Future: API documentation, development guides

### `/assets/` - Game Assets
Placeholder for future game assets:
- Sprite images
- Sound files
- Configuration files
- Theme resources

## 🚀 Launcher Scripts

### Cross-Platform Launchers
- **run_game.py**: Universal Python launcher with error handling
- **run_game.sh**: Linux/macOS shell script with dependency checking
- **run_game.bat**: Windows batch file with automatic setup

### Features
- ✅ Python version checking (3.6+ required)
- ✅ Dependency verification and installation
- ✅ User-friendly error messages
- ✅ Platform-specific optimizations

## 📦 Package Files

### Development Files
- **requirements.txt**: Minimal dependencies (pygame, numpy)
- **setup.py**: Package configuration for PyPI distribution
- **.gitignore**: Comprehensive Python project ignore rules

### Documentation Files
- **README.md**: Main project documentation with badges and screenshots
- **INSTALL.md**: Detailed installation instructions for all platforms
- **LICENSE**: MIT license for open-source distribution

## 🎯 Usage

### Quick Start
```bash
# Clone and run
git clone <repository-url>
cd enhanced-retro-cricket
python run_game.py
```

### Platform-Specific
```bash
# Linux/macOS
./run_game.sh

# Windows
run_game.bat

# Direct Python
python src/enhanced_cricket.py
```

## 🔧 Development

### Adding New Features
1. Modify source files in `/src/`
2. Update documentation in `/docs/`
3. Add screenshots to `/screenshots/`
4. Update README.md with new features

### Testing
- Run the game on multiple platforms
- Generate new screenshots with `screenshot_generator.py`
- Verify all launcher scripts work correctly

This structure provides a professional, maintainable, and user-friendly project layout suitable for open-source distribution and collaborative development.
