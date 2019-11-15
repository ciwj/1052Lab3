import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(20,GPIO.HIGH)
time.sleep(1)
GPIO.output(20, GPIO.LOW)
GPIO.output(21,GPIO.HIGH)
time.sleep(1)
GPIO.output(21, GPIO.LOW)