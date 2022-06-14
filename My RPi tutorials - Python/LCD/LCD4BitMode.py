from Adafruit_CharLCD import Adafruit_CharLCD
import time

lcd = Adafruit_CharLCD(rs=4, en=17, d4=27, d5=22, d6=5, d7=6, cols=16, lines=2)

def main():
    while True:
        lcd.clear()
        message = input('Enter any message : ')
        if message:
            lcd.message(str(message))
        else:
            lcd.clear()
        time.sleep(2)
def reset():
    lcd.clear()
    lcd.show_cursor(False)
    
if __name__ == '__main__':
    print('Program is starting...')
    try:
        main()
    except KeyboardInterrupt:
        reset()