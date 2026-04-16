from gpiozero import DigitalInputDevice, LED
from signal import pause

alcohol = DigitalInputDevice(17)
led = LED(27)


def detected():
    print("Alcohol detected!")
    led.on()


def not_detected():
    print("No alcohol")
    led.off()


alcohol.when_activated = detected
alcohol.when_deactivated = not_detected

pause()


"""
MQ3 Sensor
Vcc → 5V (Pin 2)
GND → GND (Pin 6)
DO (Digital Output) → GPIO 17 (Pin 11)

LED (Indicator)
Long leg (Anode) → GPIO 27 (Pin 13)
Short leg (Cathode) → Resistor → GND
"""
