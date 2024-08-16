#Raspberry Pi main code to enable and disable the Armor Bay Picos
#Code is ran in Python 3

import time
import RPi.GPIO as GPIO

hours_list = [31,33,35,8,10,12,16,18,24,26,32,36]

#pinout setups
GPIO.setmode(GPIO.BOARD)
GPIO.setup(hours_list, GPIO.OUT, initial=GPIO.LOW)

while True:
    hour = time.strftime('%H')
    
    if int(hour) > 12:
        hour = int(hour)-12
        
    #hour
    suit = int(hour)
    suit_pin = hours_list[suit]
    print(suit)
    print(suit_pin)
    
    GPIO.output(hours_list, GPIO.LOW)
    GPIO.output(suit_pin, GPIO.HIGH)
