import random
import pygame
import numpy as np

class MazeGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Mia and Eva's 3D Maze Escape")
        
        # 3D Maze Setup (9 rooms)
        self.maze_layout = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        
        # Player setup
        self.player_pos = [0, 0, 0]  # Starting position
        self.keys_collected = 0
        self.total_keys = 2
        
        # Key locations (randomly placed)
        self.key_locations = self._generate_key_locations()
        
    def _generate_key_locations(self):
        """Randomly place 2 keys in different rooms"""
        keys = []
        while len(keys) < self.total_keys:
            room = [random.randint(0, 2), random.randint(0, 2)]
            if room not in keys:
                keys.append(room)
        return keys
    
    def move_player(self, direction):
        """Move player in 3D maze"""
        x, y, z = self.player_pos
        
        # Implement movement logic with maze boundaries
        if direction == 'up' and y > 0:
            self.player_pos[1] -= 1
        elif direction == 'down' and y < 2:
            self.player_pos[1] += 1
        elif direction == 'left' and x > 0:
            self.player_pos[0] -= 1
        elif direction == 'right' and x < 2:
            self.player_pos[0] += 1
        
        # Check if key is collected
        self._check_key_collection()
    
    def _check_key_collection(self):
        """Check if player is on a key location"""
        current_room = [self.player_pos[0], self.player_pos[1]]
        if current_room in self.key_locations:
            self.key_locations.remove(current_room)
            self.keys_collected += 1
    
    def is_game_won(self):
        """Check if game is won (all keys collected)"""
        return self.keys_collected == self.total_keys
    
    def render(self):
        """Render 3D maze view"""
        # Placeholder for 3D rendering
        pass
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_player('up')
                    elif event.key == pygame.K_DOWN:
                        self.move_player('down')
                    elif event.key == pygame.K_LEFT:
                        self.move_player('left')
                    elif event.key == pygame.K_RIGHT:
                        self.move_player('right')
            
            self.render()
            
            if self.is_game_won():
                print("Congratulations! Mia and Eva escaped!")
                running = False
            
            pygame.display.flip()
        
        pygame.quit()

def main():
    game = MazeGame()
    game.run()

if __name__ == "__main__":
    main()
