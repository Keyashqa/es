import time
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)


led = LED(17)
led.blink()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    GPIO.output(17, True)
    time.sleep(1)
    GPIO.output(17, False)
    time.sleep(1)


"""
Long leg (Anode) → GPIO (e.g., GPIO 17)
Short leg (Cathode) → Resistor → GND
"""
