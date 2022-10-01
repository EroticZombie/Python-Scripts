import RPi.GPIO as GPIO
import datetime
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT) #1 with tap humitifier
GPIO.setup(20, GPIO.OUT) #2 lights
GPIO.setup(21, GPIO.OUT) #3 currently not in use

GPIO.output(26, 0)
GPIO.output(20, 0)
GPIO.output(21, 0)

lights = False
humid = False

while True:
    time.sleep(5)
    my_date = datetime.datetime.now() 
    current_hour = my_date.hour

    if current_hour > 8 and current_hour < 22:

        if lights:
            pass

        else:
            GPIO.output(20, 1)
            lights = True

    else:
        if lights:
            GPIO.output(20, 0)
            lights = False  

        else:
            pass

    if current_hour%6 == 0:
        if humid:
            pass

        else:
            GPIO.output(26, 1)
            humid = True

    else:
        if humid:
            GPIO.output(26, 0)
            humid = False

        else:
            pass


GPIO.cleanup()