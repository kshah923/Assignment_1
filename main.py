# Kevin Shah
# February 8, 2021
# Assignment_1

import numpy as np
import matplotlib.pyplot as plt

# 1 Period of Sine and Cosine Functions
time = np.arange(0, 2*np.pi, 0.1)
sin = np.sin(time)
cos = np.cos(time)
tan = np.tan(time)
plt.plot(time, sin, time, cos)

# title, legend, color_coding
plt.title('Trig Graphs')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axhline(linewidth=1, color='black')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
