#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

hours_list = [6,13,19,14,18,23,25,20,9,21,11,17]
HOMER_pin =  12

#pinout setups
GPIO.setup(hours_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(HOMER_pin, GPIO.OUT)

HOMER = GPIO.PWM(HOMER_pin, 1000)
HOMER.start(0)
PWM_direction = 1

while True:
    hour_string = time.strftime('%H')
    hour = int(hour_string)
    
    if hour >= 12:
        hour = hour-12

    suit = int(hour)
    suit_pin = hours_list[suit]

    if hour == 0:
        GPIO.output(hours_list[0], GPIO.HIGH)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 1:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.HIGH)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 2:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.HIGH)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 3:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.HIGH)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 4:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.HIGH)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 5:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.HIGH)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 6:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.HIGH)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 7:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.HIGH)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 8:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.HIGH)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 9:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.HIGH)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 10:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.HIGH)
        GPIO.output(hours_list[11], GPIO.LOW)
    elif hour == 11:
        GPIO.output(hours_list[0], GPIO.LOW)
        GPIO.output(hours_list[1], GPIO.LOW)
        GPIO.output(hours_list[2], GPIO.LOW)
        GPIO.output(hours_list[3], GPIO.LOW)
        GPIO.output(hours_list[4], GPIO.LOW)
        GPIO.output(hours_list[5], GPIO.LOW)
        GPIO.output(hours_list[6], GPIO.LOW)
        GPIO.output(hours_list[7], GPIO.LOW)
        GPIO.output(hours_list[8], GPIO.LOW)
        GPIO.output(hours_list[9], GPIO.LOW)
        GPIO.output(hours_list[10], GPIO.LOW)
        GPIO.output(hours_list[11], GPIO.HIGH)
        
    if PWM_direction == 1:
        for duty_cycle in range(0,101,1):
            HOMER.ChangeDutyCycle(duty_cycle)
            time.sleep(.01)
            #print(duty_cycle)
        PWM_direction = 0
    elif PWM_direction == 0:
        for duty_cycle in range(100,-1,-1):
            HOMER.ChangeDutyCycle(duty_cycle)
            time.sleep(.01)
            #print(duty_cycle)
        PWM_direction = 1
