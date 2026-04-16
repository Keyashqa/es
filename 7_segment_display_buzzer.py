from gpiozero import LED, Button, PWMOutputDevice
from signal import pause
from time import sleep

pins = [13, 6, 16, 20, 21, 19, 26]
segments = [LED(pin) for pin in pins]

digits = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]


def display(num):
    for seg, val in zip(segments, digits[num]):
        if val:
            seg.on()
        else:
            seg.off()


button = Button(5)
buzzer = PWMOutputDevice(18)

count = 0


def update():
    global count
    count = (count + 1) % 10
    display(count)
    buzzer.value = count / 9


button.when_pressed = update

display(0)
pause()


"""
7-Segment (Common Cathode)

Segments → GPIO (via resistor)

Segment	GPIO
a	13
b	6
c	16
d	20
e	21
f	19
g	26

Common pins → GND

Button
One side → GPIO 5
Other side → GND

Buzzer (3-pin)
Signal → GPIO 18
Vcc → 3.3V
GND → GND
"""
