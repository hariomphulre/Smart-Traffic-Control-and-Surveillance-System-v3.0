# import time
# import sys
# import lgpio
# import json
# import os
# import drivers
# from time import sleep

# display=drivers.Lcd()

# try:
#     while True:
#         # input size must be <=16
#         print("writing to display")
#         display.lcd_display_string("Success!",1)
#         sleep(10)

# except Keyboardinterrupt:
#     print("Cleaning up!")
#     display.lcd_clear()


#/////////////////////////////////////////////////////

# import smbus

# bus = smbus.SMBus(1)
# address = 0x27  # Replace with your detected address
# bus.write_byte(address, 0x00)  # This should not throw error

#/////////////////////////////////////////////////////////

# import board
# import digitalio
# import adafruit_character_lcd.character_lcd as characterlcd

# lcd_rs = digitalio.DigitalInOut(board.D7)
# lcd_en = digitalio.DigitalInOut(board.D8)
# lcd_d4 = digitalio.DigitalInOut(board.D25)
# lcd_d5 = digitalio.DigitalInOut(board.D24)
# lcd_d6 = digitalio.DigitalInOut(board.D23)
# lcd_d7 = digitalio.DigitalInOut(board.D18)

# lcd_columns = 16
# lcd_rows = 2

# lcd = characterlcd.Character_LCD_Mono(
#     lcd_rs, lcd_en,
#     lcd_d4, lcd_d5, lcd_d6, lcd_d7,
#     lcd_columns, lcd_rows
# )

# lcd.message = "Hello, Pi LCD!"


#////////////////////// I2C ///////////////////////
# import board
# import busio
# import adafruit_character_lcd.character_lcd_i2c as character_lcd

# # LCD size
# lcd_columns = 16
# lcd_rows = 2

# # Initialize I2C bus.
# i2c = busio.I2C(board.SCL, board.SDA)

# # Initialize the LCD class with detected address (0x27)
# lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, address=0x27)

# lcd.message = "Hello,\nI2C LCD works!"
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as characterlcd

# LCD size
lcd_columns = 16
lcd_rows = 2

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize LCD class with I2C address
lcd = characterlcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, address=0x27)

# Clear any previous content
lcd.clear()

# Write your message
lcd.message = "Test I2C LCD\nAdjust contrast!"




