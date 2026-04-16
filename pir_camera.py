from picamera import PiCamera
from gpiozero import MotionSensor, LED
from time import sleep
from datetime import datetime

pir = MotionSensor(17)
led = LED(27)
camera = PiCamera()

camera.resolution = (1024, 768)
camera.brightness = 60
camera.contrast = 20

print("System Ready")

while True:
    pir.wait_for_motion()
    print("Motion Detected!")

    for i in range(4):
        led.on()
        sleep(0.3)
        led.off()
        sleep(0.2)

    for i in range(2):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"motion_{timestamp}_{i}.jpg"
        camera.capture(filename)
        sleep(1)

    pir.wait_for_no_motion()
""" 
    PIR
    VCC 5V
    OUT GND
    GND GPIO17

    LED
    Long leg (Anode) → GPIO 27 (through resistor)
    Short leg (Cathode) → GND

    Camera CSI port

    camera configuration : sudo raspi-config
"""
