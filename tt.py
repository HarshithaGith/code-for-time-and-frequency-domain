import numpy as np
import matplotlib.pyplot as plt

# Generate a time-domain signal
duration = 1.0  # Duration of the signal in seconds
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, duration, int(fs*duration), endpoint=False)  # Time vector
f = 10  # Frequency of the signal
signal = np.sin(2 * np.pi * f * t)

# Perform Fourier Transform
freq_spectrum = np.fft.fft(signal)
freq_spectrum = np.abs(freq_spectrum)  # Take the absolute value for visualization

# Calculate corresponding frequencies
freq = np.fft.fftfreq(len(signal), d=1/fs)

# Plot the time-domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time Domain')

# Plot the frequency spectrum
plt.subplot(2, 1, 2)
plt.plot(freq, freq_spectrum)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Domain')

# Adjust subplot spacing
plt.tight_layout()

# Display the plots
plt.show()
