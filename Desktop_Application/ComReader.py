import serial
import threading


class ComReader(threading.Thread):
    def __init__(self, port, game):
        self.port = port
        self.game = game
        super(ComReader, self).__init__()
        try:
            self.ser = serial.Serial(port, 9600, timeout=0)
        except (OSError, serial.SerialException):
            exit(0)
        self.data = [0, 0, 0, 0, 0]
        self.last_data = [0, 0, 0, 0, 0]

    def run(self):
        while self.game.on:
            help1 = self.last_data
            self.last_data = self.data
            help2 = str(self.ser.read(5))
            if len(help2) > 5:
                self.data = help2[2] + help2[3] + help2[4] + help2[5] + help2[6]
            else:
                self.last_data = help1
            if self.data[4] == '1':
                print(self.data)
        self.ser.close()
