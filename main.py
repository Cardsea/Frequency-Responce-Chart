import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.signal import chirp

# CONFIG
duration = 2  # total sweep time in seconds
fs = 44100  # sample rate
f_start = 20  # start frequency
f_end = 20000  # end frequency

# Generate chirp (sweep) signal
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
sweep = 0.5 * chirp(t, f0=f_start, f1=f_end, t1=duration, method='logarithmic')

print("Starting continuous sweep...")

# Play and record simultaneously
recording = sd.playrec(sweep, samplerate=fs, channels=1, dtype='float64')
sd.wait()

# Split recorded signal into short time slices and analyze
window_size = int(fs * 0.1)  # 100ms window
frequencies = []
amplitudes = []

for i in range(0, len(t), window_size):
    segment = recording[i:i + window_size]
    if len(segment) < window_size:
        continue
    rms = np.sqrt(np.mean(segment**2))
    # Approximate frequency at this window
    freq = f_start * (f_end / f_start) ** (i / len(t))
    frequencies.append(freq)
    amplitudes.append(rms)

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, amplitudes, marker='o')
plt.title("Continuous Frequency Sweep Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (RMS)")
plt.grid(True, which='both', ls='--')
plt.show()