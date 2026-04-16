from gpiozero import LED, Button
from signal import pause

button = Button(5)
led = LED(27)

button.when_pressed = led.toggle

pause()






















"""
LED
Anode (long leg) → GPIO 17 (through resistor)
Cathode (short leg) → GND
Button
One side → GPIO 2
Other side → GND
"""