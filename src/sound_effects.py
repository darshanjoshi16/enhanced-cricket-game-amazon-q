import pygame
import numpy as np

class SoundEffects:
    def __init__(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        self.sounds = {}
        self.generate_sounds()
    
    def generate_tone(self, frequency, duration, sample_rate=22050):
        """Generate a simple tone"""
        frames = int(duration * sample_rate)
        arr = np.zeros((frames, 2))
        
        for i in range(frames):
            wave = np.sin(2 * np.pi * frequency * i / sample_rate)
            arr[i] = [wave, wave]
        
        # Fade in/out to avoid clicks
        fade_frames = int(0.1 * sample_rate)
        for i in range(fade_frames):
            arr[i] *= i / fade_frames
            arr[frames - 1 - i] *= i / fade_frames
        
        return (arr * 32767).astype(np.int16)
    
    def generate_sounds(self):
        """Generate all game sound effects"""
        try:
            # Hit sound - satisfying "thwack"
            hit_sound = self.generate_tone(200, 0.2)
            self.sounds['hit'] = pygame.sndarray.make_sound(hit_sound)
            
            # Wicket sound - descending tone
            wicket_frames = int(0.5 * 22050)
            wicket_arr = np.zeros((wicket_frames, 2))
            for i in range(wicket_frames):
                freq = 400 - (i / wicket_frames) * 300  # 400Hz to 100Hz
                wave = np.sin(2 * np.pi * freq * i / 22050) * 0.5
                wicket_arr[i] = [wave, wave]
            self.sounds['wicket'] = pygame.sndarray.make_sound((wicket_arr * 32767).astype(np.int16))
            
            # Boundary sound - ascending celebration
            boundary_frames = int(0.8 * 22050)
            boundary_arr = np.zeros((boundary_frames, 2))
            for i in range(boundary_frames):
                freq = 300 + (i / boundary_frames) * 200  # 300Hz to 500Hz
                wave = np.sin(2 * np.pi * freq * i / 22050) * 0.3
                wave += np.sin(2 * np.pi * freq * 1.5 * i / 22050) * 0.2  # Harmony
                boundary_arr[i] = [wave, wave]
            self.sounds['boundary'] = pygame.sndarray.make_sound((boundary_arr * 32767).astype(np.int16))
            
            # Power-up sound
            powerup_sound = self.generate_tone(440, 0.3)
            self.sounds['powerup'] = pygame.sndarray.make_sound(powerup_sound)
            
            # Milestone celebration sound (longer, more elaborate)
            milestone_frames = int(1.5 * 22050)
            milestone_arr = np.zeros((milestone_frames, 2))
            for i in range(milestone_frames):
                # Create a fanfare-like sound
                base_freq = 440
                wave = 0
                # Multiple harmonics for richness
                for harmonic in [1, 1.5, 2, 2.5]:
                    freq = base_freq * harmonic
                    wave += np.sin(2 * np.pi * freq * i / 22050) * (0.2 / harmonic)
                
                # Add some modulation for excitement
                modulation = 1 + 0.3 * np.sin(2 * np.pi * 5 * i / 22050)
                wave *= modulation
                milestone_arr[i] = [wave, wave]
            self.sounds['milestone'] = pygame.sndarray.make_sound((milestone_arr * 32767).astype(np.int16))
            
        except Exception as e:
            print(f"Could not generate sounds: {e}")
            # Create silent sounds as fallback
            silent = np.zeros((1000, 2), dtype=np.int16)
            for key in ['hit', 'wicket', 'boundary', 'powerup', 'milestone']:
                self.sounds[key] = pygame.sndarray.make_sound(silent)
    
    def play(self, sound_name):
        """Play a sound effect"""
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except:
                pass  # Silently fail if sound can't play
