import time
import random
from lcd import LCD
from news import get_headlines

def main():
    try:
        lcd = LCD()
        while True:
            headlines = get_headlines()
            random.shuffle(headlines)

            for headline in headlines:
                print(headline)
                lcd.write(headline)
                time.sleep(3)
    except KeyboardInterrupt:
        lcd.clear()

if __name__ == '__main__':
    main()
