# micropython_esp32_ssd1331
This MicroPython Sample script is for 96*64 pixels 16 bit color OLED. (SSD1331 controler) 
I was checked this script by ESP32 DevBoard and micropython v1.9.4 

## Dependency libralies:
  * ssd1331.py
  * rgb.py

     These py files are here. => https://github.com/adafruit/micropython-adafruit-rgb-display

 ## IF YOU RUN THIS SCRIPT, NEED IMAGE FILE. (and transfer ESP32)
  * Windows bitmap format
  * 96*64 pixels
  * 24bit color
  * name -> test.bmp

## SPI Pins [OLED -> ESP32 DevBord]
  * GND -> GND 
  * VCC -> 3V3
  * SCL -> P12
  * SDA -> P13
  * RES -> P14
  * DC  -> P15
  * CS  -> P16

## 3D Printing OLED Case
use .stl files for 3D printing.