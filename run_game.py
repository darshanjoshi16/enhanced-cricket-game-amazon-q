#!/usr/bin/env python3
"""
Enhanced Retro Cricket Game Launcher
Simple script to run the game with proper error handling.
"""

import sys
import os

def main():
    """Main launcher function"""
    print("🏏 Enhanced Retro Cricket Game")
    print("=" * 35)
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Error: Python 3.6 or higher is required")
        print(f"   Current version: {sys.version}")
        return 1
    
    # Add src directory to path
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    sys.path.insert(0, src_path)
    
    try:
        # Import and run the game
        from enhanced_cricket import EnhancedCricket
        print("✅ Game modules loaded successfully")
        print("🎮 Starting game...")
        print("\nControls:")
        print("  A/D or Arrow Keys - Move batsman")
        print("  SPACE - Power shot")
        print("  S - Defensive shot")
        print("  ESC - Menu/Quit")
        print("\nEnjoy the game! 🏏\n")
        
        game = EnhancedCricket()
        game.run()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Install required dependencies:")
        print("   pip install pygame numpy")
        print("2. Make sure you're in the correct directory")
        print("3. Check that all files are present")
        return 1
        
    except Exception as e:
        print(f"❌ Game Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check your graphics drivers")
        print("2. Close other applications")
        print("3. Try running with: python -u run_game.py")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
