from ADCDevice import *
import time
import math

adc = ADCDevice()
delayTime = 1

def setup():
    global adc
    if adc.detectI2C(0x48):
        adc = PCF8591()
    else:
        print('Incorrect I2C Address')
        exit(-1)
        
def main():
    while True:
        value = adc.analogRead(0)
        voltage = value/255.0*5.0
        Rt = 10 * voltage / (5.0 - voltage)
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)
        tempC = tempK - 273.15
        print('ADC : %d, Voltage : %.3f, Temperature : %.2f'%(value,voltage,tempC))
        time.sleep(delayTime)
        
def reset():
    adc.close()
    
if __name__ == '__main__':
    print('Program is starting')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()