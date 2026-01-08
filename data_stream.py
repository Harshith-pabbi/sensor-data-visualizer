import random
import time

def sensor_stream():
    time.sleep(0.01)
    return random.uniform(20, 100)
