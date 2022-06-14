import RPi.GPIO as GPIO
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from ADCDevice import *
import pygame
import thingspeak

adc = ADCDevice()
lcd  = Adafruit_CharLCD(rs=26, en=21, d4=22, d5=20, d6=19, d7=13, cols=16, lines=2)
delayTime = 1
digitalPin = 18
redPin = 27
greenPin = 6

pygame.init()
pygame.mixer.music.load("intruder.mp3")

channel_id = 1645363
write_key = 'AUA9S93BC6Q0LAKX'

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(redPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(greenPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(digitalPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global adc
    if (adc.detectI2C(0x48)):
        adc = PCF8591()
    else:
        print('Incorrect I2C address')
        lcd.message('Incorrect I2C\naddress')

def measure(channel):
       value = adc.analogRead(0)
       if GPIO.input(digitalPin) == False:
            pygame.mixer.music.stop()
            print('Analog voltage : %.3f'%(value/255.0*5.0))
            lcd.show_cursor(True)
            lcd.set_cursor(0, 0)
            lcd.message('No Fire.......\n')
            lcd.message('Voltage : %.3f V'%(value/255.0*5.0))
            GPIO.output(redPin, GPIO.LOW)
            GPIO.output(greenPin, GPIO.HIGH)
       else:
            GPIO.output(redPin, GPIO.HIGH)
            GPIO.output(greenPin, GPIO.LOW)
            pygame.mixer.music.play()
            print('Fire detected\n Analog Voltage : %.3f'%(value/255.0*5.0))
            lcd.clear()
            lcd.set_cursor(0, 0)
            lcd.message('Fire detected!!!\n')
            lcd.message('Voltage : %.3f V'%(value/255.0*5.0))
       response = channel.update({'field1':(value/255.0*5.0)})
       
def destroy():
    pygame.mixer.music.stop()
    GPIO.cleanup()
    adc.close()

def main():
    setup()
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
         measure(channel)
         time.sleep(delayTime)
    
if True:
    try:
        main()
    except KeyboardInterrupt:
        destroy()