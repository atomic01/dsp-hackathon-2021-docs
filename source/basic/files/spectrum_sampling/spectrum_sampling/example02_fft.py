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

## We run DTFT first
exec(open("./example01_dtft.py").read())

## Find FFT

#
# NOTE
# We will now call `fft` with no additional parameters.
#
X_fft = fft(x)

# Bin axis
k = np.arange(0,len(X_fft))

## Plot the spectrum
plt.figure(spectrumFig)

# Amplitude spectrum
plt.subplot(2,1,1)
plt.stem(2*math.pi*k/len(k), np.abs(X_fft), linefmt='r', basefmt=' ')

# Phase spectrum
plt.subplot(2,1,2)
plt.stem(2*math.pi*k/len(k), np.angle(X_fft), linefmt='r', basefmt=' ')

plt.show(block=False)

input('Example 02 complete.')
