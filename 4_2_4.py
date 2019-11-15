import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

pin1 = GPIO.PWM(21,25)
pin1.start(0)
pin2 = GPIO.PWM(20,25)
pin2.start(0)

GPIO.output(25, GPIO.HIGH)  
for x in range(1,51):
    pin1.ChangeDutyCycle(x)
    time.sleep(0.05)

GPIO.output(25, GPIO.LOW)
pin1.stop()
time.sleep(2)
GPIO.output(25, GPIO.HIGH)  

for x in range(1,51):
    pin2.ChangeDutyCycle(x)
    time.sleep(0.05)

GPIO.output(25, GPIO.LOW)
pin2.stop()
GPIO.cleanup()
