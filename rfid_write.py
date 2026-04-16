import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input("Enter data to write: ")
    print("Place RFID tag near reader")
    reader.write(text)
    print("Data written successfully")

finally:
    GPIO.cleanup()























"""
    GPIO numbers
    SDA 8
    SCK 11
    MOSI 10
    MISO 9
    RST 25
    Vcc 3.3V
"""
