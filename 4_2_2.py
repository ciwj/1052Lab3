import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pin = GPIO.PWM(21,25)
pin.start(0)
pin.ChangeDutyCycle(0)

for x in range(1,51):
    pin.ChangeDutyCycle(x)
    time.sleep(0.05)

pin.stop()
GPIO.cleanup()
