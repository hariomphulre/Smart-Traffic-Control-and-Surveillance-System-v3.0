import time
import sys
import lgpio
import json
import os
import Adafruit_CharLCD as LCD

H = lgpio.gpiochip_open(0)

lcd_pin=[12,7,8,21,20,16]

lcd=LCD.Adafruit_CharLCD(12,7,8,21,20,16,0,16,2)

lcd.message("Success")