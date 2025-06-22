# Installation Guide

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Quick Install

### Option 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/enhanced-retro-cricket.git
cd enhanced-retro-cricket

# Install dependencies
pip install -r requirements.txt

# Run the game
python src/enhanced_cricket.py
```

### Option 2: Using conda

```bash
# Create a new conda environment
conda create -n cricket-game python=3.8
conda activate cricket-game

# Clone and install
git clone https://github.com/yourusername/enhanced-retro-cricket.git
cd enhanced-retro-cricket
pip install -r requirements.txt

# Run the game
python src/enhanced_cricket.py
```

### Option 3: System Package Manager

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3-pygame python3-numpy
git clone https://github.com/yourusername/enhanced-retro-cricket.git
cd enhanced-retro-cricket
python3 src/enhanced_cricket.py
```

#### macOS (using Homebrew):
```bash
brew install python
pip3 install pygame numpy
git clone https://github.com/yourusername/enhanced-retro-cricket.git
cd enhanced-retro-cricket
python3 src/enhanced_cricket.py
```

#### Windows:
```bash
# Install Python from python.org
# Then in Command Prompt:
pip install pygame numpy
git clone https://github.com/yourusername/enhanced-retro-cricket.git
cd enhanced-retro-cricket
python src/enhanced_cricket.py
```

## Troubleshooting

### Common Issues:

1. **pygame not found**: 
   ```bash
   pip install --upgrade pygame
   ```

2. **numpy not available (sound effects disabled)**:
   ```bash
   pip install numpy
   ```

3. **Permission errors on Linux**:
   ```bash
   sudo apt install python3-dev
   pip install --user pygame numpy
   ```

4. **Audio issues**:
   - The game will run without sound if numpy is not available
   - Install numpy for full audio experience

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/enhanced-retro-cricket.git
cd enhanced-retro-cricket

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run the game
python src/enhanced_cricket.py
```

## System Requirements

- **Minimum**: Python 3.6, 512MB RAM, 50MB disk space
- **Recommended**: Python 3.8+, 1GB RAM, 100MB disk space
- **Graphics**: Any system capable of running Pygame
- **Audio**: Optional (numpy required for sound effects)

## Verified Platforms

- ✅ Ubuntu 20.04+
- ✅ Windows 10+
- ✅ macOS 10.14+
- ✅ Raspberry Pi OS
- ✅ Arch Linux
- ✅ CentOS 8+

## Performance Tips

- Close other applications for better performance
- Use fullscreen mode for optimal experience
- Adjust difficulty settings if experiencing lag
- Ensure graphics drivers are up to date
