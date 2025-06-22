@echo off
REM Enhanced Retro Cricket Game - Windows Launcher

echo 🏏 Enhanced Retro Cricket Game
echo ================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.6 or higher from python.org
    pause
    exit /b 1
)

REM Check Python version
python -c "import sys; exit(0 if sys.version_info >= (3,6) else 1)" >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 3.6 or higher is required
    python --version
    pause
    exit /b 1
)

REM Check if required packages are installed
echo 🔍 Checking dependencies...
python -c "import pygame, numpy" >nul 2>&1
if errorlevel 1 (
    echo ❌ Missing dependencies. Installing...
    pip install pygame numpy
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        echo Please run: pip install pygame numpy
        pause
        exit /b 1
    )
)

echo ✅ All dependencies satisfied
echo 🎮 Starting Enhanced Retro Cricket...
echo.

REM Run the game
python run_game.py

echo.
echo Thanks for playing! 🏏
pause
