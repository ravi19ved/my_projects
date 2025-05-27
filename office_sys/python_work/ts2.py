import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)


# Apply a Hann window to the signal
window = np.hanning(len(y))
y_windowed = y * window

# Plot the original and windowed signals
plt.plot(x, y, label='Original Signal')
plt.plot(x, y_windowed, label='Windowed Signal')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Hann Windowed Signal')
plt.show()
