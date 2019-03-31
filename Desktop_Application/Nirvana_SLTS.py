import pygame


class Button(object):

    def __init__(self, position, time):
        self.pos = position
        if position == 0:
            self.color = (255, 0, 0)
            self.x = 60
        elif position == 1:
            self.color = (0, 255, 0)
            self.x = 180
        elif position == 2:
            self.color = (0, 0, 255)
            self.x = 300
        elif position == 3:
            self.x = 420
            self.color = (255, 200, 200)
        self.y = time
        self.r = 30
        self.w = 20
        self.check = False
class Buttons(object):

    def get_butt():
        buttons = []
        delay = -50
        # Intro
        buttons.append((0, 670 - 9 * 2 * 119 - int(2 * 14.875) - delay+40))
        buttons.append((0, 670 - 9 * 2 * 119 - int(10 * 14.875) - delay+40))
        buttons.append((2, 670 - 10 * 2 * 119 - int(4 * 14.875) - delay))
        buttons.append((2, 670 - 10 * 2 * 119 - int(8 * 14.875) - delay))
        buttons.append((2, 670 - 10 * 2 * 119 - int(12 * 14.875) - delay))
        buttons.append((1, 670 - 11 * 2 * 119 - int(2 * 14.875) - delay))
        buttons.append((1, 670 - 11 * 2 * 119 - int(10 * 14.875) - delay))
        buttons.append((2, 670 - 12 * 2 * 119 - int(4 * 14.875) - delay))
        buttons.append((2, 670 - 12 * 2 * 119 - int(8 * 14.875) - delay))
        buttons.append((2, 670 - 12 * 2 * 119 - int(12 * 14.875) - delay))
        for i in range(1,4):
            buttons.append((0, 670 - (9+i*4) * 2 * 119 - int(2*14.875) - delay))
            buttons.append((0, 670 - (9+i*4) * 2 * 119 - int(10*14.875) - delay))
            buttons.append((2, 670 - (10 + i * 4) * 2 * 119 - int(4*14.875) - delay))
            buttons.append((2, 670 - (10+i*4) * 2 * 119 - int(8*14.875) - delay))
            buttons.append((2, 670 - (10+i*4) * 2 * 119 - int(12*14.875) - delay))
            buttons.append((1, 670 - (11+i*4) * 2 * 119 - int(2*14.875) - delay))
            buttons.append((1, 670 - (11+i*4) * 2 * 119 - int(10*14.875) - delay))
            buttons.append((2, 670 - (12 + i * 4) * 2 * 119 - int(4*14.875) - delay))
            buttons.append((2, 670 - (12+i*4) * 2 * 119 - int(8*14.875) - delay))
            buttons.append((2, 670 - (12+i*4) * 2 * 119 - int(12*14.875) - delay))
        # Verse 1
        buttons.append((2, 670 - (9 + 4 * 4) * 2 * 119 - int(14 * 14.875) - delay+20))
        buttons.append((3, 670 - (9 + 4 * 4) * 2 * 119 - int(18 * 14.875) - delay+20))
        buttons.append((2, 670 - (9 + 5 * 4) * 2 * 119 - int(14*14.875) - delay))
        buttons.append((3, 670 - (9 + 5 * 4) * 2 * 119 - int(18*14.875) - delay))
        for i in range(6,8):
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - int(14*14.875)))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - int(18*14.875)))

            buttons.append((2, 670 - (9 + 8 * 4) * 2 * 119 - int(14*14.875) - delay-100))
            buttons.append((3, 670 - (9 + 8 * 4) * 2 * 119 - int(18*14.875) - delay-100))
            buttons.append((2, 670 - (9 + 9 * 4) * 2 * 119 - int(14 * 14.875) - delay - 130))
            buttons.append((3, 670 - (9 + 9 * 4) * 2 * 119 - int(18 * 14.875) - delay - 130))

        for i in range(10,14):
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 12 * int(14.875) - delay-12*i-5))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 20 * int(14.875) - delay-12*i-5))
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 28 * int(14.875) - delay-12*i-10))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 36 * int(14.875) - delay-12*i-10))
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 44 * int(14.875) - delay-12*i-30))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 52 * int(14.875) - delay-12*i-30))
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 60 * int(14.875) - delay-12*i-50))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 68 * int(14.875) - delay-12*i-50))

        # Intro
        delay = 20
        for i in range(0,6):
            buttons.append((0, 670 - (66+i*4) * 2 * 119 - int(2*14.875) - delay - i*22))
            buttons.append((0, 670 - (66+i*4) * 2 * 119 - int(10*14.875) - delay - i*22))
            buttons.append((2, 670 - (67 + i * 4) * 2 * 119 - int(4*14.875) - delay - i*22))
            buttons.append((2, 670 - (67+i*4) * 2 * 119 - int(8*14.875) - delay - i*22))
            buttons.append((2, 670 - (67+i*4) * 2 * 119 - int(12*14.875) - delay - i*22))
            buttons.append((1, 670 - (68+i*4) * 2 * 119 - int(2*14.875) - delay - i*22))
            buttons.append((1, 670 - (68+i*4) * 2 * 119 - int(10*14.875) - delay - i*22))
            buttons.append((2, 670 - (69 + i * 4) * 2 * 119 - int(4*14.875) - delay - i*22))
            buttons.append((2, 670 - (69+i*4) * 2 * 119 - int(8*14.875) - delay - i*22))
            buttons.append((2, 670 - (69+i*4) * 2 * 119 - int(12*14.875) - delay - i*22))
        return buttons


class Nslts(object):

    def __init__(self, game):
        self.points = 0
        self.game = game
        self.vel = 2
        self.buttons = []
        for b in Buttons.get_butt():
            self.buttons.append(Button(b[0],b[1]))
    def tick(self):
        # Physic
        for b in self.buttons:
            b.y += self.vel
        # Handle events elements
        for b in self.buttons:
            if b.y > 780:
                self.buttons.remove(b)
    def draw(self):
        # Draw buttons
        for b in self.buttons:
            if b.check:
                pygame.draw.circle(self.game.screen, b.color, (b.x, b.y), b.r, b.r)
                pygame.draw.circle(self.game.screen, (0,0,0), (b.x, b.y), 10, 2)
            else:
                pygame.draw.circle(self.game.screen,b.color,(b.x,b.y),b.r,b.w)