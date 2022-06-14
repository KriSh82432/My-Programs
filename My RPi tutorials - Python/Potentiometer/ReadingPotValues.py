from ADCDevice import *
import time

adc = ADCDevice()
delayTime = 0.1

def setup():
    global adc
    if adc.detectI2C(0x48):
        adc = PCF8591()
    else:
        print('Inocrrect I2C Address')
        exit(-1)
        
def main():
    while True:
      value = adc.analogRead(0)
      voltage = value/255.0*5.0
      print('Analog value : %d, Voltage : %.3f'%(value,voltage))
      time.sleep(delayTime)

def reset():
    adc.close()

if __name__ == '__main__':
    print('Program is starting..')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()

















