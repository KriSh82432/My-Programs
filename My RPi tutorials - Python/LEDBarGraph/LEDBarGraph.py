import RPi.GPIO as GPIO
import time
 
ledPins = [4, 17, 27, 22, 5, 6, 13, 2, 3, 8]
delayTime = 0.02

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPins, GPIO.OUT, initial = GPIO.HIGH)
    
def main():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(delayTime)
            GPIO.output(pin, GPIO.HIGH)
        for pin in ledPins[::-1]:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(delayTime)
            GPIO.output(pin, GPIO.HIGH)
  
def reset():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()