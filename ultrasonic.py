import sqlite3
import time
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=24, trigger=23, max_distance=3.0)

DATABASE_NAME = "walking_stats.db"

MAX_DETECTION_DIST = 250
MIN_DETECTION_DIST = 20


def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            avg_speed REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def log_session(avg_speed):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sessions (avg_speed) VALUES (?)",
        (avg_speed,)
    )

    conn.commit()
    conn.close()
    print("Logged avg speed:", round(avg_speed, 2), "cm/s")


init_db()

session_speeds = []
last_dist = None
last_time = None

try:
    while True:
        current_dist = sensor.distance * 100
        current_time = time.time()

        if MIN_DETECTION_DIST < current_dist < MAX_DETECTION_DIST:
            if last_dist is not None and last_time is not None:
                delta_d = abs(current_dist - last_dist)
                delta_t = current_time - last_time

                if delta_t > 0:
                    speed = delta_d / delta_t

                    if 0 < speed < 500:
                        session_speeds.append(speed)

            last_dist = current_dist
            last_time = current_time

        else:
            if len(session_speeds) > 5:
                avg_speed = sum(session_speeds) / len(session_speeds)
                log_session(avg_speed)

            session_speeds = []
            last_dist = None
            last_time = None

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped")


"""
HC-SR04 Sensor
Sensor Pin	Raspberry Pi
Vcc	5V (Pin 2)
GND	GND (Pin 6)
TRIG	GPIO 23 (Pin 16)
ECHO	GPIO 24 (Pin 18)
"""
