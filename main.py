import time
from lcd import LCD

def main():
    try:
        lcd = LCD()
        lcd.write('hello world, this is great')
        time.sleep(10)
    except KeyboardInterrupt:
        lcd.clear()

if __name__ == '__main__':
    main()
