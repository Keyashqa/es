import time
import board
import adafruit_bmp280

i2c = board.I2C()

sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

sensor.sea_level_pressure = 1013.25

print("BMP280 Sensor Initialized Successfully!")
print("---------------------------------------")

while True:
    try:
        temp = sensor.temperature
        press = sensor.pressure
        alt = sensor.altitude

        print(f"Temperature: {temp:.2f} °C")
        print(f"Pressure:    {press:.2f} hPa")
        print(f"Altitude:    {alt:.2f} meters")
        print("---------------------------------------")

    except Exception as e:
        print(f"Sensor Error: {e}")

    time.sleep(2)


"""
BMP280 Sensor (I2C)
Vcc → 3.3V (Pin 1) 
GND → GND (Pin 6)
SDA → GPIO 2 (Pin 3)
SCL → GPIO 3 (Pin 5)
"""
