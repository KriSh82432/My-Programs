import RPi.GPIO as GPIO
import time
import random

ledPins  = [13, 19, 26]
delayTime = 0.5

def setup():
    global pwmRed, pwmBlue, pwmGreen
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPins, GPIO.OUT, initial = GPIO.HIGH)
    pwmRed = GPIO.PWM(ledPins[0], 2000)
    pwmGreen = GPIO.PWM(ledPins[1], 2000)
    pwmBlue = GPIO.PWM(ledPins[2], 2000)
    pwmRed.start(0)
    pwmBlue.start(0)
    pwmGreen.start(0)
    
def setColor(rVal, gVal, bVal):
    pwmRed.ChangeDutyCycle(rVal)
    pwmGreen.ChangeDutyCycle(gVal)
    pwmBlue.ChangeDutyCycle(bVal)
    
def main():
    while True:
        r = random.randint(0, 100)
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        setColor(r, g, b)
        print('Red : %d, Green : %d, Blue : %d'%(r, g, b))
        time.sleep(delayTime)
        
def reset():
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()
    