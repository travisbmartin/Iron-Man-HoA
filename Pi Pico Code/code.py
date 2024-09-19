# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# OLED DISPLAY: https://educ8s.tv/part/OLED096

from random import randrange
import time
import board
import busio
import pwmio
import displayio
import digitalio
import adafruit_displayio_ssd1306
import adafruit_imageload
import bitmaptools

ten_pins = ['1','1','1','1','1']
minute_pins = ['1','1','1','1']

station_enable = digitalio.DigitalInOut(board.GP18)
station_enable.direction = digitalio.Direction.INPUT
station_enable.pull = digitalio.Pull.DOWN

ten_pins[0] = pwmio.PWMOut(board.GP2, frequency = 1000)
ten_pins[1] = pwmio.PWMOut(board.GP3, frequency = 1000)
ten_pins[2] = pwmio.PWMOut(board.GP4, frequency = 1000)
ten_pins[3] = pwmio.PWMOut(board.GP5, frequency = 1000)
ten_pins[4] = pwmio.PWMOut(board.GP6, frequency = 1000)

minute_pins[0] = pwmio.PWMOut(board.GP7, frequency = 1000)
minute_pins[1] = pwmio.PWMOut(board.GP8, frequency = 1000)
minute_pins[2] = pwmio.PWMOut(board.GP9, frequency = 1000)
minute_pins[3] = pwmio.PWMOut(board.GP10, frequency = 1000)

penta_light = digitalio.DigitalInOut(board.GP22)
penta_light.direction = digitalio.Direction.OUTPUT

for i in range(0,4):
    ten_pins[i].duty_cycle = 0

for i in range(0,3):
    minute_pins[i].duty_cycle = 0

seconds = 0
minutes = 0
minutes2 = 0

displayio.release_displays()

sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

image, palette = adafruit_imageload.load("/arc_reactor_2.bmp",
    bitmap=displayio.Bitmap, palette=displayio.Palette)

palette.make_transparent(0)
# Create a TileGrid to hold the bitmap
sprite = displayio.TileGrid(image, pixel_shader=palette, width = 1, height = 1, tile_width = 64, tile_height = 64)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(sprite)

# Add the Group to the Display

source_index = 0

while True:
    display.root_group = group
    group.x = 32
    penta_light.value = True
    while station_enable.value == True:
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
            minutes2 = minutes2 + 1
    
        if minutes2 >= 10:
            minutes2 = minutes2 - 10

    #prep bits
        if minutes2 == 0:
            minute_pins[0].duty_cycle = 0
            minute_pins[1].duty_cycle = 0
            minute_pins[2].duty_cycle = 0
            minute_pins[3].duty_cycle = 0

        elif minutes2 == 1:
            minute_pins[0].duty_cycle = 750
            minute_pins[1].duty_cycle = 0
            minute_pins[2].duty_cycle = 0
            minute_pins[3].duty_cycle = 0
            
        elif minutes2 == 2:
            minute_pins[0].duty_cycle = 0
            minute_pins[1].duty_cycle = 750
            minute_pins[2].duty_cycle = 0
            minute_pins[3].duty_cycle = 0

        elif minutes2 == 3:
            minute_pins[0].duty_cycle = 750
            minute_pins[1].duty_cycle = 750
            minute_pins[2].duty_cycle = 0
            minute_pins[3].duty_cycle = 0
            
        elif minutes2 == 4:
            minute_pins[0].duty_cycle = 0
            minute_pins[1].duty_cycle = 0
            minute_pins[2].duty_cycle = 750
            minute_pins[3].duty_cycle = 0
            
        elif minutes2 == 5:
            minute_pins[0].duty_cycle = 750
            minute_pins[1].duty_cycle = 0
            minute_pins[2].duty_cycle = 750
            minute_pins[3].duty_cycle = 0
            
        elif minutes2 == 6:
            minute_pins[0].duty_cycle = 0
            minute_pins[1].duty_cycle = 750
            minute_pins[2].duty_cycle = 750
            minute_pins[3].duty_cycle = 0
            
        elif minutes2 == 7:
            minute_pins[0].duty_cycle = 750
            minute_pins[1].duty_cycle = 750
            minute_pins[2].duty_cycle = 750
            minute_pins[3].duty_cycle = 0
            
        elif minutes2 == 8:
            minute_pins[0].duty_cycle = 0
            minute_pins[1].duty_cycle = 0
            minute_pins[2].duty_cycle = 0
            minute_pins[3].duty_cycle = 750
 
        elif minutes2 == 9:
            minute_pins[0].duty_cycle = 750
            minute_pins[1].duty_cycle = 0
            minute_pins[2].duty_cycle = 0
            minute_pins[3].duty_cycle = 750
            
        if minutes < 10:
            ten_pins[0].duty_cycle = 0
            ten_pins[1].duty_cycle = 0
            ten_pins[2].duty_cycle = 0
            ten_pins[3].duty_cycle = 0
            ten_pins[4].duty_cycle = 0

        elif minutes >= 10 and minutes < 20:
            ten_pins[0].duty_cycle = 750
            ten_pins[1].duty_cycle = 0
            ten_pins[2].duty_cycle = 0
            ten_pins[3].duty_cycle = 0
            ten_pins[4].duty_cycle = 0

        elif minutes >= 20 and minutes < 30:
            ten_pins[0].duty_cycle = 750
            ten_pins[1].duty_cycle = 750
            ten_pins[2].duty_cycle = 0
            ten_pins[3].duty_cycle = 0
            ten_pins[4].duty_cycle = 0

        elif minutes >= 30 and minutes < 40:
            ten_pins[0].duty_cycle = 750
            ten_pins[1].duty_cycle = 750
            ten_pins[2].duty_cycle = 750
            ten_pins[3].duty_cycle = 0
            ten_pins[4].duty_cycle = 0
            
        elif minutes >= 40 and minutes < 50:
            ten_pins[0].duty_cycle = 750
            ten_pins[1].duty_cycle = 750
            ten_pins[2].duty_cycle = 750
            ten_pins[3].duty_cycle = 750
            ten_pins[4].duty_cycle = 0

        elif minutes >= 50:
            ten_pins[0].duty_cycle = 750
            ten_pins[1].duty_cycle = 750
            ten_pins[2].duty_cycle = 750
            ten_pins[3].duty_cycle = 750
            ten_pins[4].duty_cycle = 750

        for i in range(1,10):
            rand = randrange(1,20,1)
            if rand == 3:
                sprite[0] = source_index % 3
                source_index += 1
            time.sleep(.05)
        seconds = seconds + .5

    ten_pins[0].duty_cycle = 0
    ten_pins[1].duty_cycle = 0
    ten_pins[2].duty_cycle = 0
    ten_pins[3].duty_cycle = 0
    ten_pins[4].duty_cycle = 0
    
    minute_pins[0].duty_cycle = 0
    minute_pins[1].duty_cycle = 0
    minute_pins[2].duty_cycle = 0
    minute_pins[3].duty_cycle = 0
    
    seconds = 0
    minutes = 0
    minutes2 = 0
