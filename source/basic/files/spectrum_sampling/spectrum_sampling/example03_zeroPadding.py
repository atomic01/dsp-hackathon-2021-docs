# ***************************************
#           DTFT example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Basic level example
#

import math
import numpy as np

import matplotlib.pyplot as plt

from scipy.fft import fft

## We run FFT first
exec(open("./example02_fft.py").read())

## Discussion
# At this point, it is evident that the DFT (found by using the FFT
# algorithm, samples the continous spectrum found by FFT.
#
# An important assumption we've made to achieve this is that the
# analyzed signal is now constrained (and periodic) in time domain.
#
# For DTFT, the signal was defined only on samples n=1:10. For all other
# samples n=-infty:infty, we had to assume a zero value.
#
# Let's put this claim to the test.

## Zero-pad the signal

x_zp = np.concatenate((x, np.zeros(10, dtype=int)))

# Sample axis
n_zp = np.arange(1,21)

## Plot the signal

plt.figure(timeFig)

plt.stem(n_zp, x_zp, linefmt='g', markerfmt='go', basefmt=' ')

plt.show(block=False)

## Find FFT

X_zp = fft(x_zp)

# Bin axis
k = np.arange(0, len(X_zp))

## Plot the spectrum

plt.figure(spectrumFig)

# Amplitude spectrum
plt.subplot(2,1,1)
plt.stem(2*math.pi*k/len(k), np.abs(X_zp), linefmt='g', markerfmt='go', basefmt=' ')

# Phase spectrum
plt.subplot(2,1,2)
plt.stem(2*math.pi*k/len(k), np.angle(X_zp), linefmt='g', markerfmt='go', basefmt=' ')

plt.show(block=False)

input("Example 03 complete.")
