import RPi.GPIO as GPIO
import time
from ADCDevice import *

adc = ADCDevice()
ledPin = 4
delayTime = 0.1

def setup():
    global adc
    global p
    if adc.detectI2C(0x48):
        adc = PCF8591()
    else:
        print('Incorrect I2C address')
        exit(-1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT, initial = GPIO.LOW)
    p = GPIO.PWM(ledPin, 500)
    p.start(0)
    
def main():
    while True:
        value = adc.analogRead(0)
        voltage = value/255.0*5.0
        p.ChangeDutyCycle(value*100/255)
        print('ADC value : %d , Voltage : %.3f'%(value,voltage))
        time.sleep(delayTime)
    
def reset():
    p.stop()
    adc.close()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()