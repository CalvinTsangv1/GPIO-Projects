import RPi.GPIO as GPIO
import time

SENSOR_PIN = 17  # HW-493 OUT pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.OUT)

while True:
    if GPIO.input(SENSOR_PIN) == 0:
        print("Object detected within range!")
    else:
        print("No object detected")
    time.sleep(1)
