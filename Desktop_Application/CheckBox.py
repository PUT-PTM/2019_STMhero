import pygame


class Check_box(object):

    def __init__(self, game):
        # Initialization
        self.game = game
        self.color = (255,255,255)
        self.lines = []
        self.lines.append(((10, 610),(470, 610)))
        self.lines.append(((10, 710),(470, 710)))
        self.lines.append(((10, 610),(10, 710)))
        self.lines.append(((470, 610),(470, 710)))



    def draw(self):
        # Draw lines
        for l in self.lines:
            pygame.draw.line(self.game.screen, self.color,l[0],l[1])