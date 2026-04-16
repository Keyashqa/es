import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

try:
    while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity

            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}%".format(
                    temperature_f, temperature_c, humidity
                )
            )

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue

        time.sleep(2.0)

except KeyboardInterrupt:
    print("Exiting script")

finally:
    dhtDevice.exit()


"""
DHT22 Pins (left → right facing front)
DHT22 Pin	Connection
Pin 1	Vcc → 3.3V (Pin 1)
Pin 2	Data → GPIO 4 (Pin 7)
Pin 3	Not used
Pin 4	GND → Pin 6
"""
