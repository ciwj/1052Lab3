import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

pin1 = GPIO.PWM(21,25)
pin1.start(0)
pin2 = GPIO.PWM(20,25)
pin2.start(0)
pin3 = GPIO.PWM(7, 200)
pin3.start(50)

time.sleep(0.5)
pin3.stop()
GPIO.output(25, GPIO.HIGH)
time.sleep(1)

for x in range(1,51):
    pin1.ChangeDutyCycle(x)
    time.sleep(0.05)

GPIO.output(25, GPIO.LOW)
pin1.stop()
time.sleep(2)
pin3.start(50)
time.sleep(0.5)
pin3.stop()
time.sleep(1)
GPIO.output(25, GPIO.HIGH)

for x in range(1,51):
    pin2.ChangeDutyCycle(x)
    time.sleep(0.05)

GPIO.output(25, GPIO.LOW)
pin2.stop()
GPIO.cleanup()


