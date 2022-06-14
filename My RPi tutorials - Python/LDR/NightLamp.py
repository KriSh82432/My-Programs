from ADCDevice import *
import RPi.GPIO as GPIO
import time

ledPin = 17
adc = ADCDevice()
delayTime = 0.01

def setup():
    global adc
    global p
    if adc.detectI2C(0x48):
        adc = PCF8591()
    else:
        print('incorrect I2C address')
        exit(-1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT, initial = GPIO.LOW)
    p = GPIO.PWM(ledPin, 2000)
    p.start(0)
    
def main():
    while True:
      value = adc.analogRead(0)
      p.ChangeDutyCycle(value*100/255)
      voltage = value/255.0*5.0
      print('ADC : %d, Voltage : %.3f'%(value,voltage))
      time.sleep(delayTime)
    
def reset():
    p.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()