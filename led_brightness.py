from gpiozero import PWMLED, Button
from signal import pause

led = PWMLED(18)
button = Button(5)

value = 0.2
INC = 0.1


def change():
    global value, INC
    if value >= 0.9:
        INC = -0.1
    elif value <= 0.1:
        INC = 0.1
    value += INC
    led.value = value


button.when_pressed = change
pause()

























"""
LED
Anode (long leg) → GPIO 17 (through resistor)
Cathode (short leg) → GND
Button
One side → GPIO 2
Other side → GND
"""