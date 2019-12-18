import pygame
import sys
import serial
import glob
import random
from Nirvana_SLTS import Nslts
from CheckBox import Check_box
from ComReader import ComReader


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class Game(object):

    def __init__(self, com):

        # Initialization
        self.ticks = 0
        self.on = 1
        self.max_tps = 119.0
        if com != 'none':
            self.com_reader = ComReader(com, self)
            self.com_reader.start()
            self.buttons = [0, 0, 0, 0]
            self.last_buttons = [0, 0, 0, 0]
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.font.init()
        pygame.init()
        self.screen = pygame.display.set_mode((480, 720))
        pygame.mixer.music.load('Nirvana - Smells Like Teens Spirit.mp3')
        self.ogien1 = pygame.image.load('ogien.gif').convert_alpha()
        self.ogien2 = pygame.image.load('ogien2.gif').convert_alpha()
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.song = Nslts(self)
        self.checkbox = Check_box(self)
        self.font = pygame.font.SysFont("comicsansms", 72)
        self.text = self.font.render("0", True, (255, 255, 255))
        self.pressed = [0, 0, 0, 0]
        pygame.mixer.music.play()

        # Game loop
        while True:
            self.ticks += 1
            self.holds = [0, 0, 0, 0]
            if self.pressed[0] > 0:
                self.pressed[0] -= 1
            if self.pressed[1] > 0:
                self.pressed[1] -= 1
            if self.pressed[2] > 0:
                self.pressed[2] -= 1
            if self.pressed[3] > 0:
                self.pressed[3] -= 1
            # Handle events
            if com == 'none':
                key = pygame.key.get_pressed()
                for b in self.song.buttons:
                    if b.hold > 0:
                        if b.y in range(650, 650 + b.hold):
                            if b.pos == 0:
                                if key[pygame.K_q]:
                                    if b.check:
                                        self.song.points += 1
                                        self.holds[0] = 1
                            if b.pos == 1:
                                if key[pygame.K_w]:
                                    if b.check:
                                        self.song.points += 1
                                        self.holds[1] = 1
                            if b.pos == 2:
                                if key[pygame.K_e]:
                                    if b.check:
                                        self.song.points += 1
                                        self.holds[2] = 1
                            if b.pos == 3:
                                if key[pygame.K_r]:
                                    if b.check:
                                        self.song.points += 1
                                        self.holds[3] = 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    for b in self.song.buttons:
                        if event.type == pygame.KEYDOWN:
                            if b.y in range(640, 681):
                                if event.key == pygame.K_q and b.pos == 0:
                                    if not b.check:
                                        b.check = True
                                        self.song.points += 100
                                        self.pressed[0] = 40
                                elif event.key == pygame.K_w and b.pos == 1:
                                    if not b.check:
                                        b.check = True
                                        self.song.points += 100
                                        self.pressed[1] = 40
                                elif event.key == pygame.K_e and b.pos == 2:
                                    if not b.check:
                                        b.check = True
                                        self.song.points += 100
                                        self.pressed[2] = 40
                                elif event.key == pygame.K_r and b.pos == 3:
                                    if not b.check:
                                        b.check = True
                                        self.song.points += 100
                                        self.pressed[3] = 40
                                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                    sys.exit(0)

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.on = 0
                        sys.exit(0)
                for b in self.song.buttons:
                    if b.y in range(640, 681):
                        help = self.buttons
                        self.buttons = self.com_reader.data
                        self.last_buttons = help
                        if self.buttons[0] == '1' and self.last_buttons[0] == '0' and b.pos == 0:
                            if not b.check:
                                b.check = True
                                self.song.points += 100
                        elif self.buttons[1] == '1' and self.last_buttons[1] == '0' and b.pos == 1:
                            if not b.check:
                                b.check = True
                                self.song.points += 100
                        elif self.buttons[2] == '1' and self.last_buttons[2] == '0' and b.pos == 2:
                            if not b.check:
                                b.check = True
                                self.song.points += 100
                        elif self.buttons[3] == '1' and self.last_buttons[3] == '0' and b.pos == 3:
                            if not b.check:
                                b.check = True
                                self.song.points += 100

                    if b.hold > 0:
                        if b.y in range(650, 650 + b.hold):
                            if self.buttons[4] == '1':
                                if not b.holded:
                                    b.holded = True
                            if b.pos == 0:
                                    if b.holded:
                                        self.song.points += 1
                                        self.holds[0] = 1
                            if b.pos == 1:
                                    if b.holded:
                                        self.song.points += 1
                                        self.holds[1] = 1
                            if b.pos == 2:
                                    if b.holded:
                                        self.song.points += 1
                                        self.holds[2] = 1
                            if b.pos == 3:
                                    if b.holded:
                                        self.song.points += 1
                                        self.holds[3] = 1

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.max_tps:
                self.tick()
                self.tps_delta -= 1/self.max_tps

            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            # End of game
            if self.ticks == 22800:
                print("Your score: "+str(self.song.points))
                self.on = 0
                pygame.quit()
                break


    def tick(self):
        self.text = self.font.render(str(self.song.points), True, (255, 255, 255))
        self.song.tick()

    def draw(self):
        self.song.draw()
        self.checkbox.draw()
        self.effects()
        text_rect = self.text.get_rect(center=(240, 40))
        self.screen.blit(self.text, text_rect)

    def effects(self):
        rand = random.randrange(6)
        if self.holds[0] or self.pressed[0]:
            if rand % 2 == 0:
                pygame.display.get_surface().blit(self.ogien1, (10, 610))
            else:
                pygame.display.get_surface().blit(self.ogien2, (10, 610))
        if self.holds[1] or self.pressed[1]:
            if rand % 2 == 0:
                pygame.display.get_surface().blit(self.ogien1, (125, 610))
            else:
                pygame.display.get_surface().blit(self.ogien2, (125, 610))
        if self.holds[2] or self.pressed[2]:
            if rand % 2 == 0:
                pygame.display.get_surface().blit(self.ogien1, (260, 610))
            else:
                pygame.display.get_surface().blit(self.ogien2, (260, 610))
        if self.holds[3] or self.pressed[3]:
            if rand % 2 == 0:
                pygame.display.get_surface().blit(self.ogien1, (375, 610))
            else:
                pygame.display.get_surface().blit(self.ogien2, (375, 610))


if __name__ == "__main__":
    while True:
        print("Available COM ports: " + str(serial_ports()))
        print("Enter the name of the COM port or type 'none' for playing on keyboard: ")
        inp = input()
        if inp == 'exit':
            break
        Game(inp)
