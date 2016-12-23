import time
from lcd import LCD

def main():
    lcd = LCD()
    lcd.write('hello')
    time.sleep(10)
    lcd.clear()

if __name__ == '__main__':
    main()
