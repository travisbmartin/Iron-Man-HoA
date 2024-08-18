# Code to be added to every Raspberry Pi Pico driving an Armor Bay
# Code used is to be ran in CircuitPython

from random import randrange
import time
import board
import busio
import displayio
import digitalio
import adafruit_displayio_ssd1306
import adafruit_imageload
import bitmaptools

ten_pins = ['1','1','1','1','1']
minute_pins = ['1','1','1','1']

station_enable = digitalio.DigitalInOut(board.GP28)
station_enable.direction = digitalio.Direction.INPUT
station_enable.pull = digitalio.Pull.DOWN

ten_pins[0] = digitalio.DigitalInOut(board.GP2)
ten_pins[1] = digitalio.DigitalInOut(board.GP3)
ten_pins[2] = digitalio.DigitalInOut(board.GP4)
ten_pins[3] = digitalio.DigitalInOut(board.GP5)
ten_pins[4] = digitalio.DigitalInOut(board.GP6)

minute_pins[0] = digitalio.DigitalInOut(board.GP7)
minute_pins[1] = digitalio.DigitalInOut(board.GP8)
minute_pins[2] = digitalio.DigitalInOut(board.GP9)
minute_pins[3] = digitalio.DigitalInOut(board.GP10)

ten_pins[0].direction = digitalio.Direction.OUTPUT
ten_pins[1].direction = digitalio.Direction.OUTPUT
ten_pins[2].direction = digitalio.Direction.OUTPUT
ten_pins[3].direction = digitalio.Direction.OUTPUT
ten_pins[4].direction = digitalio.Direction.OUTPUT

minute_pins[0].direction = digitalio.Direction.OUTPUT
minute_pins[1].direction = digitalio.Direction.OUTPUT
minute_pins[2].direction = digitalio.Direction.OUTPUT
minute_pins[3].direction = digitalio.Direction.OUTPUT

for i in range(0,4):
    ten_pins[i].value = False

for i in range(0,3):
    minute_pins[i].value = False

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
    while station_enable.value == False:
        if seconds == 3:
            seconds = 0
            minutes = minutes + 1
            minutes2 = minutes2 + 1
    
        if minutes2 >= 10:
            minutes2 = minutes2 - 10

    #prep bits
        minones = '{0:04b}'.format(int(minutes2))
    
        for i in range(0,4):
            minute_pins[i].value = int(minones[i])
            print(int(minones[i]))
    
        print()
    
        if minutes < 10:
            ten_pins[0].value = False
            ten_pins[1].value = False
            ten_pins[2].value = False
            ten_pins[3].value = False
            ten_pins[4].value = False
            print(0)
        elif minutes >= 10 and minutes < 20:
            ten_pins[0].value = True
            ten_pins[1].value = False
            ten_pins[2].value = False
            ten_pins[3].value = False
            ten_pins[4].value = False
            print(1)
        elif minutes >= 20 and minutes < 30:
            ten_pins[0].value = True
            ten_pins[1].value = False
            ten_pins[2].value = False
            ten_pins[3].value = True
            ten_pins[4].value = False
            print(1,2)
        elif minutes >= 30 and minutes < 40:
            ten_pins[0].value = True
            ten_pins[1].value = True
            ten_pins[2].value = False
            ten_pins[3].value = True
            ten_pins[4].value = False
            print(1,2,3)
        elif minutes >= 40 and minutes < 50:
            ten_pins[0].value = True
            ten_pins[1].value = True
            ten_pins[2].value = True
            ten_pins[3].value = True
            ten_pins[4].value = False
            print(1,2,3,4)
        elif minutes >= 50:
            ten_pins[0].value = True
            ten_pins[1].value = True
            ten_pins[2].value = True
            ten_pins[3].value = True
            ten_pins[4].value = True
            print(1,2,3,4,5)
        print()
        if minutes >= 60:
            minutes = 0
        
        
        for i in range(1,10):
            rand = randrange(1,20,1)
            if rand == 3:
                sprite[0] = source_index % 3
                source_index += 1
            time.sleep(.05)
        seconds = seconds + .5
        print(seconds)

for i in range(0,4):
    ten_pins[i].value = False

for i in range(0,3):
    minute_pins[i].value = False
