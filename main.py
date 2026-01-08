import matplotlib
matplotlib.use('TkAgg')

from data_stream import sensor_stream
from theme_engine import ThemeEngine
from visualizer import Visualizer
import matplotlib.pyplot as plt

theme = ThemeEngine()
viz = Visualizer(window_size=60)
update_speed = 0.05  # configurable (0.01-0.1)

print("Press Ctrl+C to stop")
print("Theme change: dark -> light -> neon")

try:
    while True:
        value = sensor_stream()
        color = theme.apply(plt)
        viz.update(value, color)
        
        if int(value) % 30 == 0:
            theme.switch('neon')
except KeyboardInterrupt:
    print("Visualization stopped")
