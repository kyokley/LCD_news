import random
from lcd import LCD, NUM_ROWS, ROW_LENGTH
from news import get_headlines

BLANK_MESSAGE = ' ' * NUM_ROWS * ROW_LENGTH
def main():
    try:
        lcd = LCD()
        while True:
            headlines = get_headlines()
            random.shuffle(headlines)

            headlines.append('')
            all_headlines = BLANK_MESSAGE.join(headlines)
            print('\n'.join(headlines))
            lcd.write(all_headlines)
    except KeyboardInterrupt:
        lcd.clear()

if __name__ == '__main__':
    main()
