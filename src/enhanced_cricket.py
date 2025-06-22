import pygame
import sys
import random
import math
try:
    import numpy as np
    from sound_effects import SoundEffects
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False
    print("NumPy not available - running without sound effects")

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
GREEN = (34, 139, 34)  # Cricket pitch green
DARK_GREEN = (0, 100, 0)  # Darker green for boundaries
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
RED = (220, 20, 60)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_BROWN = (205, 133, 63)

# Game settings
DIFFICULTY_LEVELS = {
    'Easy': {'ball_speed': 3, 'spawn_delay': 180, 'accuracy': 0.8},
    'Medium': {'ball_speed': 5, 'spawn_delay': 120, 'accuracy': 0.6},
    'Hard': {'ball_speed': 7, 'spawn_delay': 90, 'accuracy': 0.4}
}

class Stadium:
    def __init__(self):
        self.boundary_radius = 300
        self.pitch_width = 200
        self.pitch_height = 400
        
    def draw(self, screen):
        # Draw stadium background
        screen.fill(DARK_GREEN)
        
        # Draw outer boundary (stadium)
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        pygame.draw.circle(screen, GREEN, (center_x, center_y), self.boundary_radius, 0)
        pygame.draw.circle(screen, WHITE, (center_x, center_y), self.boundary_radius, 3)
        
        # Draw pitch
        pitch_rect = pygame.Rect(
            center_x - self.pitch_width // 2,
            center_y - self.pitch_height // 2,
            self.pitch_width,
            self.pitch_height
        )
        pygame.draw.rect(screen, LIGHT_BROWN, pitch_rect)
        pygame.draw.rect(screen, WHITE, pitch_rect, 2)
        
        # Draw stumps at both ends
        self.draw_stumps(screen, center_x, center_y - self.pitch_height // 2 + 20)  # Bowler's end
        self.draw_stumps(screen, center_x, center_y + self.pitch_height // 2 - 20)  # Batsman's end
        
        # Draw crease lines
        pygame.draw.line(screen, WHITE, 
                        (center_x - 30, center_y + self.pitch_height // 2 - 30),
                        (center_x + 30, center_y + self.pitch_height // 2 - 30), 2)
        
    def draw_stumps(self, screen, x, y):
        for i in range(3):
            pygame.draw.rect(screen, WHITE, (x - 15 + i * 10, y - 15, 3, 30))
        # Draw bails
        pygame.draw.line(screen, WHITE, (x - 15, y - 15), (x + 15, y - 15), 2)

class Bowler:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 40
        self.animation_frame = 0
        self.bowling_action = False
        self.bowl_timer = 0
        
    def update(self):
        self.animation_frame += 1
        if self.bowling_action:
            self.bowl_timer += 1
            if self.bowl_timer > 30:  # Reset bowling action
                self.bowling_action = False
                self.bowl_timer = 0
    
    def start_bowling(self):
        self.bowling_action = True
        self.bowl_timer = 0
        
    def draw(self, screen):
        # Draw bowler body
        color = BLUE if not self.bowling_action else RED
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        
        # Draw head
        pygame.draw.circle(screen, BROWN, (self.x + self.width//2, self.y - 10), 8)
        
        # Draw arms (animated during bowling)
        if self.bowling_action:
            arm_angle = math.sin(self.bowl_timer * 0.5) * 45
            arm_x = self.x + self.width//2 + math.cos(math.radians(arm_angle)) * 15
            arm_y = self.y + 10 + math.sin(math.radians(arm_angle)) * 15
            pygame.draw.line(screen, BROWN, (self.x + self.width//2, self.y + 10), (arm_x, arm_y), 3)
        else:
            pygame.draw.line(screen, BROWN, (self.x + self.width//2, self.y + 10), (self.x + self.width//2 + 10, self.y + 20), 3)

class Batsman:
    def __init__(self, x, y):
        self.width = 30
        self.height = 50
        self.x = x - self.width // 2
        self.y = y - self.height
        self.speed = 6
        self.stance = 'ready'  # ready, swing, defensive
        self.swing_timer = 0
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        # Movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
            
        # Batting actions
        if keys[pygame.K_SPACE]:
            self.stance = 'swing'
            self.swing_timer = 20
        elif keys[pygame.K_s]:
            self.stance = 'defensive'
        else:
            self.stance = 'ready'
            
        # Update swing timer
        if self.swing_timer > 0:
            self.swing_timer -= 1
            if self.swing_timer == 0:
                self.stance = 'ready'
        
        # Keep within boundaries
        if self.x < SCREEN_WIDTH//2 - 100:
            self.x = SCREEN_WIDTH//2 - 100
        elif self.x + self.width > SCREEN_WIDTH//2 + 100:
            self.x = SCREEN_WIDTH//2 + 100 - self.width
    
    def draw(self, screen):
        # Draw batsman body
        color = BLUE
        if self.stance == 'swing':
            color = RED
        elif self.stance == 'defensive':
            color = YELLOW
            
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        
        # Draw head
        pygame.draw.circle(screen, BROWN, (self.x + self.width//2, self.y - 8), 6)
        
        # Draw bat based on stance
        bat_length = 25
        if self.stance == 'swing':
            bat_angle = -45 + (self.swing_timer * 4)
        elif self.stance == 'defensive':
            bat_angle = 10
        else:
            bat_angle = 0
            
        bat_end_x = self.x + self.width//2 + bat_length * math.cos(math.radians(bat_angle))
        bat_end_y = self.y + self.height//2 - bat_length * math.sin(math.radians(bat_angle))
        pygame.draw.line(screen, WHITE, 
                        (self.x + self.width//2, self.y + self.height//2),
                        (bat_end_x, bat_end_y), 4)

class Fielder:
    def __init__(self, x, y, position_name):
        self.original_x = x  # Store original position
        self.original_y = y
        self.x = x
        self.y = y
        self.width = 20
        self.height = 30
        self.position_name = position_name
        self.target_x = x
        self.target_y = y
        self.speed = 2
        self.is_chasing = False
        
    def update(self, ball=None):
        # Simple AI: move towards ball if it's hit
        if ball and ball.speed_y < 0:  # Ball is going up (hit)
            self.target_x = ball.x
            self.target_y = ball.y
            self.is_chasing = True
        else:
            # Return to original position
            self.target_x = self.original_x
            self.target_y = self.original_y
            self.is_chasing = False
            
        # Move towards target
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 5:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed
    
    def reset_position(self):
        """Reset fielder to original position"""
        self.x = self.original_x
        self.y = self.original_y
        self.target_x = self.original_x
        self.target_y = self.original_y
        self.is_chasing = False
    
    def draw(self, screen):
        color = RED if self.is_chasing else GRAY
        pygame.draw.rect(screen, color, (int(self.x), int(self.y), self.width, self.height))
        pygame.draw.circle(screen, BROWN, (int(self.x + self.width//2), int(self.y - 5)), 4)

class Ball:
    def __init__(self):
        self.radius = 6
        self.speed_y = 4
        self.speed_x = 0
        self.color = RED
        self.trail = []  # Initialize trail first
        self.power_up = None
        self.reset_position()  # Now call reset_position
        
    def reset_position(self):
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        self.x = center_x + random.randint(-20, 20)
        self.y = center_y - 180  # Start from bowler's end
        self.speed_y = 4
        self.speed_x = random.uniform(-1, 1)
        self.trail.clear()
        
        # Random power-up chance
        if random.random() < 0.1:  # 10% chance
            self.power_up = random.choice(['fast', 'slow', 'curve'])
        else:
            self.power_up = None
    
    def update(self):
        # Apply power-up effects
        if self.power_up == 'fast':
            speed_multiplier = 1.5
            self.color = YELLOW
        elif self.power_up == 'slow':
            speed_multiplier = 0.7
            self.color = BLUE
        elif self.power_up == 'curve':
            speed_multiplier = 1.0
            self.speed_x += math.sin(pygame.time.get_ticks() * 0.01) * 0.1
            self.color = (255, 0, 255)  # Purple
        else:
            speed_multiplier = 1.0
            self.color = RED
        
        # Update position
        self.x += self.speed_x
        self.y += self.speed_y * speed_multiplier
        
        # Add to trail
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 10:
            self.trail.pop(0)
        
        # Boundary checks
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.speed_x *= -0.8
            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        
        # Check boundaries
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        distance_from_center = math.sqrt((self.x - center_x)**2 + (self.y - center_y)**2)
        
        if distance_from_center > 300:  # Hit boundary
            self.reset_position()
            return "boundary"
        elif self.y > SCREEN_HEIGHT // 2 + 180:  # Missed by batsman
            self.reset_position()
            return "wicket"
        elif self.y < SCREEN_HEIGHT // 2 - 200:  # Ball went too high (6 runs)
            self.reset_position()
            return "six"
            
        return None
    
    def check_collision(self, batsman):
        bat_x = batsman.x + batsman.width // 2
        bat_y = batsman.y + batsman.height // 2
        bat_width = 35 if batsman.stance == 'swing' else 25
        bat_height = 10
        
        if (bat_x - bat_width//2 <= self.x <= bat_x + bat_width//2 and
            bat_y - bat_height//2 <= self.y + self.radius <= bat_y + bat_height//2 and
            self.speed_y > 0):
            
            hit_position = (self.x - bat_x) / (bat_width // 2)
            hit_position = max(-1, min(1, hit_position))
            
            # Power depends on stance
            if batsman.stance == 'swing':
                power = 8
            elif batsman.stance == 'defensive':
                power = 4
            else:
                power = 6
                
            self.speed_y = -power
            self.speed_x = hit_position * 5
            
            # Add randomness
            self.speed_x += random.uniform(-0.5, 0.5)
            self.speed_y += random.uniform(-1, 0.5)
            
            return True
        return False
    
    def draw(self, screen):
        # Draw trail
        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail)))
            trail_color = (*self.color[:3], alpha) if len(self.color) == 3 else self.color
            pygame.draw.circle(screen, trail_color, pos, max(1, self.radius - (len(self.trail) - i)))
        
        # Draw ball
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw power-up indicator
        if self.power_up:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius + 2, 1)
class EnhancedCricket:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Enhanced Retro Cricket")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game objects
        self.stadium = Stadium()
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.bowler = Bowler(center_x - 12, center_y - 180)
        self.batsman = Batsman(center_x, center_y + 160)
        self.ball = Ball()
        
        # Create fielders
        self.fielders = []
        fielder_positions = [
            (center_x - 150, center_y - 100, "Mid-off"),
            (center_x + 150, center_y - 100, "Mid-on"),
            (center_x - 200, center_y, "Square leg"),
            (center_x + 200, center_y, "Point"),
            (center_x - 100, center_y + 100, "Fine leg"),
            (center_x + 100, center_y + 100, "Third man"),
            (center_x, center_y - 250, "Long-off"),
            (center_x, center_y + 250, "Long-on")
        ]
        
        for x, y, name in fielder_positions:
            self.fielders.append(Fielder(x, y, name))
        
        # Game state
        self.score = 0
        self.outs = 3
        self.boundaries = 0
        self.sixes = 0
        self.game_over = False
        self.high_score = 0
        self.difficulty = 'Medium'
        self.ball_spawn_timer = 0
        self.combo_multiplier = 1
        self.consecutive_hits = 0
        
        # Celebration system
        self.celebration_timer = 0
        self.celebration_type = None
        self.last_milestone = 0  # Track last milestone achieved
        
        # UI
        self.font = pygame.font.Font(None, 28)
        self.large_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 20)
        
        # Sound effects
        if SOUND_AVAILABLE:
            try:
                self.sound_effects = SoundEffects()
            except:
                self.sound_effects = None
                print("Sound effects disabled")
        else:
            self.sound_effects = None
        
        # Menu state
        self.show_menu = True
        self.menu_selection = 0
        self.menu_options = ['Start Game', 'Difficulty: Medium', 'High Score: 0', 'Quit']
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.show_menu:
                    self.handle_menu_input(event.key)
                elif self.game_over:
                    if event.key == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_m:
                        self.show_menu = True
                        self.game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                else:
                    if event.key == pygame.K_ESCAPE:
                        self.show_menu = True
                    elif event.key == pygame.K_p:
                        self.toggle_pause()
    
    def handle_menu_input(self, key):
        if key == pygame.K_UP:
            self.menu_selection = (self.menu_selection - 1) % len(self.menu_options)
        elif key == pygame.K_DOWN:
            self.menu_selection = (self.menu_selection + 1) % len(self.menu_options)
        elif key == pygame.K_RETURN:
            if self.menu_selection == 0:  # Start Game
                self.show_menu = False
                self.restart_game()
            elif self.menu_selection == 1:  # Difficulty
                difficulties = list(DIFFICULTY_LEVELS.keys())
                current_index = difficulties.index(self.difficulty)
                self.difficulty = difficulties[(current_index + 1) % len(difficulties)]
                self.menu_options[1] = f'Difficulty: {self.difficulty}'
            elif self.menu_selection == 3:  # Quit
                self.running = False
    
    def restart_game(self):
        self.score = 0
        self.outs = 3
        self.boundaries = 0
        self.sixes = 0
        self.game_over = False
        self.ball_spawn_timer = 0
        self.combo_multiplier = 1
        self.consecutive_hits = 0
        self.celebration_timer = 0
        self.celebration_type = None
        self.last_milestone = 0
        self.ball.reset_position()
        
        # Reset all fielders to original positions
        for fielder in self.fielders:
            fielder.reset_position()
        
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.batsman.x = center_x - self.batsman.width // 2
        self.batsman.y = center_y + 160 - self.batsman.height
    
    def update_combo(self):
        if self.consecutive_hits >= 5:
            self.combo_multiplier = 3
        elif self.consecutive_hits >= 3:
            self.combo_multiplier = 2
        else:
            self.combo_multiplier = 1
    
    def update(self):
        if self.show_menu or self.game_over:
            return
        
        # Update celebration timer
        if self.celebration_timer > 0:
            self.celebration_timer -= 1
            
        # Update game objects
        self.batsman.update()
        self.bowler.update()
        
        # Update fielders
        for fielder in self.fielders:
            fielder.update(self.ball)
        
        # Ball spawning logic
        self.ball_spawn_timer += 1
        spawn_delay = DIFFICULTY_LEVELS[self.difficulty]['spawn_delay']
        
        if self.ball_spawn_timer > spawn_delay:
            self.bowler.start_bowling()
            self.ball_spawn_timer = 0
        
        # Update ball
        ball_event = self.ball.update()
        
        # Handle ball events
        if ball_event == "wicket":
            if self.sound_effects:
                self.sound_effects.play('wicket')
            self.outs -= 1
            self.consecutive_hits = 0
            self.combo_multiplier = 1
            self.reset_fielders()  # Reset fielders after each ball
            if self.outs <= 0:
                self.game_over = True
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.menu_options[2] = f'High Score: {self.high_score}'
        elif ball_event == "boundary":
            self.boundaries += 1
            self.score += 4 * self.combo_multiplier
            self.consecutive_hits += 1
            self.update_combo()
            self.trigger_celebration('boundary')
            self.reset_fielders()  # Reset fielders after each ball
            self.check_milestones()
        elif ball_event == "six":
            self.sixes += 1
            self.score += 6 * self.combo_multiplier
            self.consecutive_hits += 1
            self.update_combo()
            self.trigger_celebration('six')
            self.reset_fielders()  # Reset fielders after each ball
            self.check_milestones()
        
        # Check collision
        if self.ball.check_collision(self.batsman):
            if self.sound_effects:
                self.sound_effects.play('hit')
            base_points = 1
            if self.batsman.stance == 'swing':
                base_points = 2
            elif self.batsman.stance == 'defensive':
                base_points = 1
                
            self.score += base_points * self.combo_multiplier
            self.consecutive_hits += 1
            self.update_combo()
            self.check_milestones()
    
    def trigger_celebration(self, celebration_type):
        """Trigger a celebration animation"""
        self.celebration_timer = 180  # 3 seconds at 60 FPS
        self.celebration_type = celebration_type
        if self.sound_effects:
            if celebration_type in ['boundary', 'six']:
                self.sound_effects.play('boundary')
            elif celebration_type in ['fifty', 'century', 'one_fifty']:
                self.sound_effects.play('milestone')  # Use special milestone sound
    
    def reset_fielders(self):
        """Reset all fielders to their original positions"""
        for fielder in self.fielders:
            fielder.reset_position()
    
    def check_milestones(self):
        """Check for scoring milestones and trigger celebrations"""
        # Check for 50 runs milestone
        if self.score >= 50 and self.last_milestone < 50:
            self.trigger_celebration('fifty')
            self.last_milestone = 50
        # Check for 100 runs milestone
        elif self.score >= 100 and self.last_milestone < 100:
            self.trigger_celebration('century')
            self.last_milestone = 100
        # Check for 150 runs milestone
        elif self.score >= 150 and self.last_milestone < 150:
            self.trigger_celebration('one_fifty')
            self.last_milestone = 150
    
    def draw(self):
        if self.show_menu:
            self.draw_menu()
        elif self.game_over:
            self.draw_game_over()
        else:
            self.draw_game()
        
        pygame.display.flip()
    
    def draw_menu(self):
        self.screen.fill(DARK_GREEN)
        
        # Title
        title = self.large_font.render("ENHANCED CRICKET", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 150))
        self.screen.blit(title, title_rect)
        
        # Menu options
        for i, option in enumerate(self.menu_options):
            color = YELLOW if i == self.menu_selection else WHITE
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, 250 + i * 50))
            self.screen.blit(text, text_rect)
        
        # Instructions
        instructions = [
            "Use Arrow Keys to navigate",
            "Press ENTER to select",
            "Game Controls:",
            "A/D or Arrow Keys - Move batsman",
            "SPACE - Power shot",
            "S - Defensive shot",
            "ESC - Menu"
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.small_font.render(instruction, True, WHITE)
            self.screen.blit(text, (50, 450 + i * 25))
    
    def draw_game(self):
        # Draw stadium and field
        self.stadium.draw(self.screen)
        
        # Draw fielders
        for fielder in self.fielders:
            fielder.draw(self.screen)
        
        # Draw game objects
        self.bowler.draw(self.screen)
        self.batsman.draw(self.screen)
        self.ball.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
    
    def draw_ui(self):
        # Score panel
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        outs_text = self.font.render(f"Outs: {self.outs}", True, WHITE)
        self.screen.blit(outs_text, (10, 40))
        
        boundaries_text = self.font.render(f"Boundaries: {self.boundaries}", True, WHITE)
        self.screen.blit(boundaries_text, (10, 70))
        
        sixes_text = self.font.render(f"Sixes: {self.sixes}", True, WHITE)
        self.screen.blit(sixes_text, (10, 100))
        
        # Combo multiplier
        if self.combo_multiplier > 1:
            combo_text = self.font.render(f"COMBO x{self.combo_multiplier}!", True, YELLOW)
            self.screen.blit(combo_text, (10, 130))
        
        # Difficulty
        diff_text = self.small_font.render(f"Difficulty: {self.difficulty}", True, WHITE)
        self.screen.blit(diff_text, (SCREEN_WIDTH - 150, 10))
        
        # High score
        high_score_text = self.small_font.render(f"High Score: {self.high_score}", True, WHITE)
        self.screen.blit(high_score_text, (SCREEN_WIDTH - 150, 30))
        
        # Power-up indicator
        if self.ball.power_up:
            power_text = self.font.render(f"Special Ball: {self.ball.power_up.upper()}", True, YELLOW)
            text_rect = power_text.get_rect(center=(SCREEN_WIDTH//2, 50))
            self.screen.blit(power_text, text_rect)
        
        # Batting stance indicator
        stance_color = WHITE
        if self.batsman.stance == 'swing':
            stance_color = RED
        elif self.batsman.stance == 'defensive':
            stance_color = BLUE
            
        stance_text = self.small_font.render(f"Stance: {self.batsman.stance.upper()}", True, stance_color)
        self.screen.blit(stance_text, (10, SCREEN_HEIGHT - 30))
        
        # Draw celebration if active
        if self.celebration_timer > 0:
            self.draw_celebration()
    
    def draw_celebration(self):
        """Draw celebration animations and messages"""
        # Create pulsing effect
        pulse = int(abs(math.sin(self.celebration_timer * 0.1)) * 50)
        
        # Celebration messages
        messages = {
            'boundary': "BOUNDARY! 4 RUNS!",
            'six': "SIX! MAXIMUM!",
            'fifty': "FIFTY! WELL PLAYED!",
            'century': "CENTURY! FANTASTIC!",
            'one_fifty': "150 RUNS! AMAZING!"
        }
        
        if self.celebration_type in messages:
            # Background flash effect
            flash_alpha = int((self.celebration_timer / 180) * 100)
            flash_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            flash_surface.set_alpha(flash_alpha)
            
            if self.celebration_type in ['boundary', 'six']:
                flash_surface.fill(YELLOW)
            else:  # Milestones
                flash_surface.fill((255, 215, 0))  # Gold color
            
            self.screen.blit(flash_surface, (0, 0))
            
            # Main celebration text
            celebration_color = (255, 255 - pulse, 0)  # Pulsing yellow-red
            celebration_text = self.large_font.render(messages[self.celebration_type], True, celebration_color)
            text_rect = celebration_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            
            # Add shadow effect
            shadow_text = self.large_font.render(messages[self.celebration_type], True, BLACK)
            shadow_rect = shadow_text.get_rect(center=(SCREEN_WIDTH//2 + 3, SCREEN_HEIGHT//2 + 3))
            self.screen.blit(shadow_text, shadow_rect)
            self.screen.blit(celebration_text, text_rect)
            
            # Additional effects for milestones
            if self.celebration_type in ['fifty', 'century', 'one_fifty']:
                # Draw stars around the text
                for i in range(8):
                    angle = (i * 45) + (self.celebration_timer * 2)
                    star_x = SCREEN_WIDTH//2 + math.cos(math.radians(angle)) * 100
                    star_y = SCREEN_HEIGHT//2 + math.sin(math.radians(angle)) * 50
                    pygame.draw.polygon(self.screen, YELLOW, [
                        (star_x, star_y - 10),
                        (star_x + 3, star_y - 3),
                        (star_x + 10, star_y - 3),
                        (star_x + 5, star_y + 2),
                        (star_x + 8, star_y + 10),
                        (star_x, star_y + 6),
                        (star_x - 8, star_y + 10),
                        (star_x - 5, star_y + 2),
                        (star_x - 10, star_y - 3),
                        (star_x - 3, star_y - 3)
                    ])
    
    def draw_game_over(self):
        # Draw game background (dimmed)
        self.draw_game()
        
        # Overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.large_font.render("GAME OVER", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 120))
        self.screen.blit(game_over_text, text_rect)
        
        # Final stats
        stats = [
            f"Final Score: {self.score}",
            f"Boundaries (4s): {self.boundaries}",
            f"Sixes: {self.sixes}",
            f"High Score: {self.high_score}",
            "",
            "Press R to restart",
            "Press M for menu",
            "Press ESC to quit"
        ]
        
        for i, stat in enumerate(stats):
            color = YELLOW if stat.startswith("High Score") and self.score == self.high_score else WHITE
            text = self.font.render(stat, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40 + i * 30))
            self.screen.blit(text, text_rect)
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

# Run the enhanced game
if __name__ == "__main__":
    game = EnhancedCricket()
    game.run()
