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
        elif len(message) <= NUM_ROWS * ROW_LENGTH:
            for i in xrange(NUM_ROWS):
                LCD1602.write(0, i, message[i * ROW_LENGTH:(i + 1) * ROW_LENGTH])

    def clear(self):
        LCD1602.clear()
