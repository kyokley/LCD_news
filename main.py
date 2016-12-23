import time
from lcd import LCD

def main():
    try:
        lcd = LCD()
        lcd.write('My name is Ozymandias, king of kings: Look on my works, ye Mighty, and despair!')
    except KeyboardInterrupt:
        lcd.clear()

if __name__ == '__main__':
    main()
