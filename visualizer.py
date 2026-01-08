import matplotlib.pyplot as plt
from collections import deque

class Visualizer:
    def __init__(self, window_size=60):
        self.buffer = deque(maxlen=window_size)
        self.fig, self.ax = plt.subplots()
    
    def update(self, value, color):
        self.buffer.append(value)
        self.ax.clear()
        self.ax.plot(list(self.buffer), color=color)
        self.ax.set_ylim(0, 120)
        plt.pause(0.001)
