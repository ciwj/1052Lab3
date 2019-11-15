import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pin1 = GPIO.PWM(20,25)
pin1.start(0)
#pin2 = GPIO.PWM(21,25)
#pin2.start(0)
pin1.ChangeDutyCycle(25)
#pin2.ChangeDutyCycle(25)
time.sleep(5)

pin1.stop()
pin2.stop()
GPIO.cleanup()