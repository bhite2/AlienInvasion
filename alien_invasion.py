import sys

import pygame

class AlienInvasion:
    
    def _init_(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.bg_color)
                    
            pygame.display.flip()
            
if __name__ == "_main_":
    ai = AlienInvasion()
    ai.run_game()
        
        