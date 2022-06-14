from Adafruit_CharLCD import Adafruit_CharLCD
import thingspeak
import time
import Adafruit_DHT

channel_id = 1644687
write_key = 'QD5PD64KZY90ZA7U' 

pin = 4
sensor = Adafruit_DHT.DHT11
lcd  = Adafruit_CharLCD(rs=26, en=21, d4=22, d5=20, d6=19, d7=13, cols=16, lines=2)
delayTime = 15

def measure(channel):
try:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity))
        lcd.clear()
        lcd.message('Temperature = {0:0.1f}*C \nHumidity = {1:0.1f}%'.format(temperature, humidity))
    else:
        print('Did not receive any reading from sensor. Please check!')
        lcd.clear()
        lcd.message('Unable to\n get data')
    response = channel.update({'field1': temperature, 'field2': humidity})
    #read = channel.get({})
    #print('Read:',read)
except:
       print("connection failure")
       lcd.clear()
       lcd.message('Connection\nFailure')
       
    
def destroy():
pass
lcd.clear()

def main():
channel = thingspeak.Channel(id=channel_id, api_key=write_key)
while True:
     measure(channel)
     time.sleep(delayTime)
     
if True:
lcd.clear()
try:
    main()
except KeyboardInterrupt:
    destroy()


    