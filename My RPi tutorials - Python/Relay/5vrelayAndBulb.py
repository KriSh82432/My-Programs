import RPi.GPIO as GPIO
import time

relay = 18
delayTime = 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay, GPIO.OUT, initial = GPIO.LOW)
    
def main():
    while True:
        GPIO.output(relay, GPIO.HIGH)
        print('NO shorted')
        time.sleep(delayTime)
        GPIO.output(relay, GPIO.LOW)
        print('NC shorted')
        time.sleep(delayTime)
        
def reset():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()