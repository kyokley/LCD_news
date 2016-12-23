import LCD1602

ROW_LENGTH = 16
NUM_ROWS = 2

class LCD(object):
    def __init__(self):
        LCD1602.init(0x27, 1)   # init(slave address, background light)
        self.messages = []

    def write(self, message):
        if len(message) <= ROW_LENGTH:
            LCD1602.write(0, 0, message)

    def clear(self):
        LCD1602.clear()
