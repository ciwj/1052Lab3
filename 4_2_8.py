import time
import RPi.GPIO as GPIO
import lcd_i2c

lcd_i2c.lcd_init()
def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(1,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pin1 = GPIO.PWM(21,25)
pin2 = GPIO.PWM(20,25)
pin3 = GPIO.PWM(7, 200)


printLCD("Press a button", "")

def clockwise():
    pin1.start(0)
    pin3.start(50)
    time.sleep(0.5)
    pin3.stop()
    time.sleep(1)
    printLCD("Going clockwise", "")
    GPIO.output(25, GPIO.HIGH)

    for x in range(1,51):
        pin1.ChangeDutyCycle(x)
        time.sleep(0.05)

    GPIO.output(25, GPIO.LOW)
    pin1.stop()
        
def counterclockwise():
    pin3.start(50)
    time.sleep(0.5)
    pin2.start(0)
    pin3.stop()
    time.sleep(1)
    printLCD("Going", "counterclockwise")
    GPIO.output(25, GPIO.HIGH)

    for x in range(1,51):
        pin2.ChangeDutyCycle(x)
        time.sleep(0.05)

    GPIO.output(25, GPIO.LOW)
    pin2.stop()
    time.sleep(2)

try:
    while True:
        if(GPIO.input(1) == GPIO.HIGH):
            print("clockwise")
            clockwise()
        
        time.sleep(0.1)
        
        if(GPIO.input(16) == GPIO.HIGH):
            print("counterclockwise")
            counterclockwise()
            
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass

printLCD("Program exited.", "")
pin1.stop()
pin2.stop()
pin3.stop()
GPIO.cleanup()
time.sleep(2)
lcd_i2c.cleanup()
