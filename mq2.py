from gpiozero import DigitalInputDevice, LED
from signal import pause

gas = DigitalInputDevice(17)
led = LED(27)

def gas_detected():
    print("Gas detected!")
    led.on()

def gas_cleared():
    print("No gas")
    led.off()

gas.when_activated = gas_detected
gas.when_deactivated = gas_cleared

pause()


















"""
MQ2 Sensor
Vcc → Pin 2 (5V)
GND → Pin 6 (GND)
DO (Digital Output) → GPIO 17

LED
Long leg (Anode) → GPIO 27 (through resistor)
Short leg (Cathode) → GND

"""
