import RPi.GPIO as GPIO
import time
import random

ledPins  = [13, 19, 26]
delayTime = 0.5

def setup():
    global pwmRed, pwmBlue, pwmGreen
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPins, GPIO.OUT, initial = GPIO.HIGH)
    pwmBlue = GPIO.PWM(ledPins[2], 75)
    pwmGreen = GPIO.PWM(ledPins[1], 75)
    pwmRed = GPIO.PWM(ledPins[0], 75)
    pwmRed.start(0)
    pwmBlue.start(0)
    pwmGreen.start(0)
    
def setColor(rVal, gVal, bVal):
    pwmRed.ChangeDutyCycle(rVal)
    pwmGreen.ChangeDutyCycle(gVal)
    pwmBlue.ChangeDutyCycle(bVal)
    
def main():
    while True:
        r = int(input('Enter Red value : '))
        g = int(input('Enter Green value  : '))
        b = int(input('Enter Blue value : '))
        if r >= 0 and r <= 255 and g >=0 and g<=255 and b>=0 and b<=255:
           setColor(r, g, b)
        else:
            print('Invalid color input, Please check')
            continue
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
    