#!/usr/bin/env python3
"""
Screenshot Generator for Enhanced Retro Cricket Game
This script captures various game states for documentation purposes.
"""

import pygame
import sys
import os
from enhanced_cricket import EnhancedCricket

def capture_screenshots():
    """Capture screenshots of different game states"""
    
    # Initialize the game
    game = EnhancedCricket()
    
    # Create screenshots directory
    screenshot_dir = "../screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    
    screenshots_to_capture = [
        {
            'name': 'main_menu',
            'description': 'Main menu with navigation options',
            'setup': lambda: setattr(game, 'show_menu', True)
        },
        {
            'name': 'gameplay',
            'description': 'Active gameplay with batsman and ball',
            'setup': lambda: setattr(game, 'show_menu', False)
        },
        {
            'name': 'boundary_celebration',
            'description': 'Boundary celebration animation',
            'setup': lambda: [
                setattr(game, 'show_menu', False),
                game.trigger_celebration('boundary')
            ]
        },
        {
            'name': 'milestone_celebration',
            'description': 'Milestone celebration (50 runs)',
            'setup': lambda: [
                setattr(game, 'show_menu', False),
                setattr(game, 'score', 50),
                game.trigger_celebration('fifty')
            ]
        },
        {
            'name': 'game_over',
            'description': 'Game over screen with final statistics',
            'setup': lambda: [
                setattr(game, 'show_menu', False),
                setattr(game, 'game_over', True),
                setattr(game, 'score', 75),
                setattr(game, 'boundaries', 8),
                setattr(game, 'sixes', 3)
            ]
        }
    ]
    
    print("🏏 Enhanced Retro Cricket - Screenshot Generator")
    print("=" * 50)
    
    for i, screenshot in enumerate(screenshots_to_capture, 1):
        print(f"\n📸 Capturing screenshot {i}/{len(screenshots_to_capture)}: {screenshot['name']}")
        print(f"   Description: {screenshot['description']}")
        
        try:
            # Setup the game state
            screenshot['setup']()
            
            # Update and draw the game
            game.update()
            game.draw()
            
            # Save screenshot
            filename = f"{screenshot_dir}/{screenshot['name']}.png"
            pygame.image.save(game.screen, filename)
            
            print(f"   ✅ Saved: {filename}")
            
        except Exception as e:
            print(f"   ❌ Error capturing {screenshot['name']}: {e}")
    
    print(f"\n🎉 Screenshot generation complete!")
    print(f"📁 Screenshots saved in: {screenshot_dir}/")
    
    # Cleanup
    pygame.quit()

def create_demo_descriptions():
    """Create descriptions for the demo screenshots"""
    
    descriptions = {
        'main_menu.png': """
# Main Menu Screenshot

The main menu showcases the game's clean interface with:
- Title: "ENHANCED CRICKET"
- Navigation options: Start Game, Difficulty selection, High Score display
- Control instructions at the bottom
- Professional dark green cricket-themed background
        """,
        
        'gameplay.png': """
# Gameplay Screenshot

Active gameplay showing:
- Stadium environment with circular boundary
- Cricket pitch with proper markings and stumps
- Humanized batsman (blue) in ready stance
- Animated bowler (blue/red during action)
- 8 fielders positioned around the ground
- Ball with trail effects
- UI showing score, outs, boundaries, and combo multiplier
- Power-up indicators and stance information
        """,
        
        'boundary_celebration.png': """
# Boundary Celebration Screenshot

Celebration animation featuring:
- "BOUNDARY! 4 RUNS!" message in large, pulsing text
- Yellow flash effect across the screen
- Shadow effects for text depth
- Celebration timer active (3 seconds)
- Score increment visible
- Fielders in motion toward the ball
        """,
        
        'milestone_celebration.png': """
# Milestone Celebration Screenshot

50-run milestone celebration showing:
- "FIFTY! WELL PLAYED!" in gold pulsing text
- Animated stars rotating around the message
- Gold background flash effect
- Enhanced visual effects for achievement
- Score display showing 50+ runs
- Special milestone fanfare audio (when available)
        """,
        
        'game_over.png': """
# Game Over Screenshot

Game over screen displaying:
- Semi-transparent overlay over the game field
- "GAME OVER" in large white text
- Final statistics: Score, Boundaries (4s), Sixes
- High score comparison with highlighting
- Control instructions: R to restart, M for menu, ESC to quit
- Professional presentation with clear readability
        """
    }
    
    # Save descriptions
    for filename, description in descriptions.items():
        desc_file = f"../screenshots/{filename.replace('.png', '_description.md')}"
        with open(desc_file, 'w') as f:
            f.write(description.strip())
    
    print("📝 Screenshot descriptions created!")

if __name__ == "__main__":
    print("🏏 Enhanced Retro Cricket - Demo Screenshot Generator")
    print("=" * 55)
    print("\nThis script captures screenshots of various game states.")
    print("Make sure the game runs properly before generating screenshots.\n")
    
    try:
        # Test if pygame and the game work
        pygame.init()
        print("✅ Pygame initialized successfully")
        
        # Generate screenshots
        capture_screenshots()
        
        # Create descriptions
        create_demo_descriptions()
        
        print("\n🎯 All demo materials generated successfully!")
        print("📁 Check the screenshots/ directory for all files.")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install pygame numpy")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure the game files are in the correct location.")
    
    finally:
        try:
            pygame.quit()
        except:
            pass
