# ***************************************
#     Discrete frequency axis example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Basic level example
#

# Here we present how the frequency of a continuous signal maps
# to its discrete signal counterpart on the [-pi,pi> frequency axis.

import math
import numpy as np

import matplotlib.pyplot as plt

from scipy.fft import fft

## Generate a sine signal with some noise 

fs=1.024e3 # Sampling frequency
N=1024 # Number of samples of sine signal
f0=32 # Signal frequency

# Time axis, normalized to fs
t=np.arange(0,N-1)/fs 

# Signal
x = np.cos(2 * np.pi * f0 * t)

noise = np.random.normal(0, .1, x.shape)
x = x + noise

## Calculate spectrum
Nfft=256

# Spacing between each FFT bin
deltaf=fs/Nfft

# Frequency axis
f=np.fft.fftfreq(Nfft,1/fs)
f=np.fft.fftshift(f)

# FFT
X=np.fft.fft(x,Nfft)
X=np.fft.fftshift(X)

## Plots

# Time domain
plt.figure()
plt.stem(t,x)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Time domain')

plt.show(block=False)

# Amplitude spectrum
plt.figure()
plt.plot(f,20*np.log10(np.abs(X)))
plt.ylabel('|X| [dB]')
plt.xlabel('f [Hz]')
plt.title('Amplitude spectrum')

plt.show()

## Discussion
# The second figure shows the amplitude spectrum of a sine signal.
# The signal was generated with central frequency of 32. (We interpret
# the time scale as being in seconds, so we say the frequency is in
# units of Hertz.)
# After discretization in 1024 points, with a sampling frequency fs, we
# obtain a discrete signal for which we observe the frequency axis in
# interval [-pi, pi>. However, knowing the sampling frequency, this axis
# can be interpreted as [-fs/2,fs/2>, which we then used when plotting
# the spectrum.

input("Example 04 complete.")
