#!/bin/bash
# Enhanced Retro Cricket Game - Linux/macOS Launcher

echo "🏏 Enhanced Retro Cricket Game"
echo "================================"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

# Check Python version
python3 -c "import sys; exit(0 if sys.version_info >= (3,6) else 1)"
if [ $? -ne 0 ]; then
    echo "❌ Python 3.6 or higher is required"
    python3 --version
    exit 1
fi

# Check if required packages are installed
echo "🔍 Checking dependencies..."
python3 -c "import pygame, numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing dependencies. Installing..."
    pip3 install pygame numpy
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        echo "Try: sudo apt install python3-pygame python3-numpy"
        exit 1
    fi
fi

echo "✅ All dependencies satisfied"
echo "🎮 Starting Enhanced Retro Cricket..."
echo ""

# Run the game
python3 run_game.py

echo ""
echo "Thanks for playing! 🏏"
