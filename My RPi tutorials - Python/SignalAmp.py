import RPi.GPIO as GPIO
import time

A = 17
B = 27
C = 20
D = 21
delayTime = 20

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(A, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(B, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(C, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(D, GPIO.OUT, initial = GPIO.LOW)
 
def bothHigh():
     GPIO.output(C, GPIO.HIGH)
     GPIO.output(D, GPIO.LOW)
    
def highLow():
    GPIO.output(C, GPIO.HIGH)
    time.sleep(delayTime)
    GPIO.output(D, GPIO.HIGH)
    
def lowHigh():
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    
def bothLow():
    GPIO.output(C, GPIO.LOW)
    GPIO.output(D, GPIO.LOW)
    
def main():
    while True:
        if GPIO.input(A) == GPIO.HIGH and GPIO.input(B) == GPIO.HIGH:
            bothHigh()
            print('A : HIGH, B : HIGH, C : HIGH, D : LOW')
        elif GPIO.input(A) == GPIO.HIGH and GPIO.input(B) == GPIO.LOW:
            highLow()
            print('A : HIGH, B : LOW, C : HIGH, D : HIGH')
        elif GPIO.input(A) == GPIO.LOW and GPIO.input(B) == GPIO.HIGH:
            print('A : LOW, B : HIGH, C : LOW, D : LOW')
            lowHigh()
        elif GPIO.input(A) == GPIO.LOW and GPIO.input(B) == GPIO.LOW:
            bothLow()
            print('A : LOW, B : LOW, C : LOW, D : LOW')
        else:
            print('Invalid input signal')
        time.sleep(0.01)
        
def reset():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting...')
    setup()
    try:
        main()
    except KeyboardInterrupt:
        reset()