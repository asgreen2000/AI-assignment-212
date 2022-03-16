import pygame
import sys
import Color


class GUI:

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    def __init__(self, data, title):
        self.data = data
        self.title = title
    def init_game(self):

        pygame.init()
        
        self.surface = pygame.display.set_mode((GUI.SCREEN_WIDTH, GUI.SCREEN_HEIGHT))
        pygame.display.set_caption(self.title)
        self.surface.fill(Color.GREEN)
        self.main_loop()

    def update_data(self, data):
        self.data = data
    
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
            
    def go_to_step(self, index):
        pass

    def dislay_grid(self):
        pass


gui = GUI([], "")

gui.init_game()