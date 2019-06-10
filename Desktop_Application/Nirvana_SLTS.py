import pygame


class Button(object):

    def __init__(self, position, time, hold = 0):
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
        self.hold = hold
        self.holded = False


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
        for i in range(1, 4):
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
        for i in range(6, 8):
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - int(14*14.875)))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - int(18*14.875)))

            buttons.append((2, 670 - (9 + 8 * 4) * 2 * 119 - int(14*14.875) - delay-100))
            buttons.append((3, 670 - (9 + 8 * 4) * 2 * 119 - int(18*14.875) - delay-100))
            buttons.append((2, 670 - (9 + 9 * 4) * 2 * 119 - int(14 * 14.875) - delay - 130))
            buttons.append((3, 670 - (9 + 9 * 4) * 2 * 119 - int(18 * 14.875) - delay - 130))

        for i in range(10, 14):
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 12 * int(14.875) - delay-12*i-5))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 20 * int(14.875) - delay-12*i-5))
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 28 * int(14.875) - delay-12*i-10))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 36 * int(14.875) - delay-12*i-10))
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 44 * int(14.875) - delay-12*i-30))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 52 * int(14.875) - delay-12*i-30))
            buttons.append((2, 670 - (9 + i * 4) * 2 * 119 - 60 * int(14.875) - delay-12*i-50))
            buttons.append((3, 670 - (9 + i * 4) * 2 * 119 - 68 * int(14.875) - delay-12*i-50))

        # Ref
        delay = 20
        for i in range(0, 6):
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
        #bridge
        buttons.append((1, 670 - 2 * 10805))
        buttons.append((0, 670 - 2 * 10829))
        buttons.append((0, 670 - 2 * 10864))
        buttons.append((2, 670 - 2 * 10918))
        buttons.append((2, 670 - 2 * (10918 + 35)))
        buttons.append((3, 670 - 2 * 10971))
        buttons.append((1, 670 - 2 * 11026))
        buttons.append((0, 670 - 2 * 11055))
        buttons.append((0, 670 - 2 * 11087))
        buttons.append((3, 670 - 2 * 11134))
        buttons.append((3, 670 - 2 * 11165))
        buttons.append((3, 670 - 2 * 11197))
        buttons.append((2, 670 - 2 * 11223))
        buttons.append((1, 670 - 2 * (10805 + 484)))
        buttons.append((0, 670 - 2 * (10829 + 484)))
        buttons.append((0, 670 - 2 * (10864 + 484)))
        buttons.append((2, 670 - 2 * (10918 + 484)))
        buttons.append((2, 670 - 2 * (10918 + 35 + 484)))
        buttons.append((3, 670 - 2 * (10971 + 484)))
        buttons.append((1, 670 - 2 * (11026 + 484+20)))
        buttons.append((0, 670 - 2 * (11055 + 484+20)))
        buttons.append((0, 670 - 2 * (11087 + 484+20)))
        buttons.append((3, 670 - 2 * (11134 + 484+20)))
        buttons.append((3, 670 - 2 * (11165 + 484+20)))
        buttons.append((3, 670 - 2 * (11197 + 484+20)))
        buttons.append((2, 670 - 2 * (11223 + 484+20)))
        return buttons


class Nslts(object):

    def __init__(self, game):
        self.points = 0
        self.game = game
        self.vel = 2
        self.buttons = []
        for b in Buttons.get_butt():
            self.buttons.append(Button(b[0], b[1]))
        self.buttons[41].hold = 238
        self.buttons[43].hold = 238
        self.buttons[45].hold = 238
        self.buttons[47].hold = 238
        self.buttons[49].hold = 238
        self.buttons[51].hold = 238
        self.buttons[53].hold = 238
        self.buttons[55].hold = 238
        self.buttons[166].hold = 75
        self.buttons[153].hold = 75
        for i in range(56, 88):
            self.buttons[i].hold = 100

    def tick(self):
        # Physic
        for b in self.buttons:
            b.y += self.vel
        # Destroy elements
        for b in self.buttons:
            if b.y > 2000:
                self.buttons.remove(b)

    def draw(self):
        # Draw buttons
        for b in self.buttons:
            if b.check:
                pygame.draw.circle(self.game.screen, b.color, (b.x, b.y), b.r, b.r)
                pygame.draw.circle(self.game.screen, (0, 0, 0), (b.x, b.y), 10, 2)
            else:
                pygame.draw.circle(self.game.screen, b.color, (b.x, b.y), b.r, b.w)

            if b.hold:
                pygame.draw.line(self.game.screen, b.color, (b.x, b.y), (b.x, b.y-b.hold), 10)
            if self.game.holds[0]:
                pygame.draw.circle(self.game.screen, (255, 255, 0), (60, 650), 10)
            if self.game.holds[1]:
                pygame.draw.circle(self.game.screen, (255, 255, 0), (180, 650), 10)
            if self.game.holds[2]:
                pygame.draw.circle(self.game.screen, (255, 255, 0), (300, 650), 10)
            if self.game.holds[3]:
                pygame.draw.circle(self.game.screen, (255, 255, 0), (420, 650), 10)
