import time
import random
from lcd import LCD, NUM_ROWS, ROW_LENGTH
from news import get_headlines

def main():
    try:
        lcd = LCD()
        while True:
            headlines = get_headlines()
            random.shuffle(headlines)

            for headline in headlines:
                print(headline)
                lcd.write('     {}'.format(headline))
                lcd.write(' ' * NUM_ROWS * ROW_LENGTH)
    except KeyboardInterrupt:
        lcd.clear()

if __name__ == '__main__':
    main()
