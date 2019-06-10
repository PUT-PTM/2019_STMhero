import serial
import threading


class ComReader(threading.Thread):
    def __init__(self, port, game):
        super(ComReader, self).__init__()
        self.port = port
        self.game = game
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
            help2 = str(self.ser.read(6))
            if len(help2) > 7:
                if help2[7] == '1':
                    self.data = help2[2] + help2[3] + help2[4] + help2[5] + help2[6]
                    print(self.data)
                else:
                    self.data = "00000"
            else:
                self.last_data = help1
        self.ser.close()
