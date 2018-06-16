#######
# This MicroPython Sample script is for 96*64 pixels 16 bit color OLED. (SSD1331 controler) 
# * I was checked this script by ESP32 DevBoard and micropython v1.9.4 
#
# Dependency libralies:
#  - ssd1331.py
#  - rgb.py
#     These py files are here. => https://github.com/adafruit/micropython-adafruit-rgb-display
#
# IF YOU RUN THIS SCRIPT, NEED IMAGE FILE. (and transfer ESP32)
#  - Windows bitmap format
#  - 96*64 pixels
#  - 24bit color
#  - name -> test.bmp
#
### SPI Pins [OLED -> ESP32 DevBord]
# GND -> GND 
# VCC -> 3V3
# SCL -> P12
# SDA -> P13
# RES -> P14
# DC  -> P15
# CS  -> P16
#

from machine import SPI,Pin
import ssd1331

# configration for SPI BUS.
spi = SPI(1, baudrate=26000000, sck=Pin(12), mosi=Pin(13)) 

# configration for color OLED.
display = ssd1331.SSD1331(spi, rst=Pin(14), dc=Pin(15), cs=Pin(16))

with open('test.bmp', 'rb') as bmp_file:

   # read offset, width, height from bitmap file header.
  bmp_file.seek(10, 0)
  offset = int.from_bytes(bmp_file.read(4), 'little')
  bmp_file.seek(4, 1)
  width = int.from_bytes(bmp_file.read(4), 'little')
  height = int.from_bytes(bmp_file.read(4), 'little')

  # skip bitmap file header
  bmp_file.seek(offset, 0)

   # read image data and transfer to oled
  for y in range(0, height):
    for x in range(0, width):
      blue = int.from_bytes(bmp_file.read(1), 'little')
      green =  int.from_bytes(bmp_file.read(1), 'little')
      red =  int.from_bytes(bmp_file.read(1), 'little')
      color = ssd1331.color565(red, green, blue)
      display.pixel(x, 63-y, color)



