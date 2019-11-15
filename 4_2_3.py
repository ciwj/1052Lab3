import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pin1 = GPIO.PWM(21,25)
pin1.start(0)
pin2 = GPIO.PWM(20,25)
pin2.start(0)

for x in range(1,51):
    pin1.ChangeDutyCycle(x)
    time.sleep(0.05)
    
pin1.stop()
time.sleep(2)

for x in range(1,51):
    pin2.ChangeDutyCycle(x)
    time.sleep(0.05)

pin2.stop()
GPIO.cleanup()
