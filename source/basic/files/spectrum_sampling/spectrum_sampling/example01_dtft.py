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

from scipy.signal import freqz

## Signal generation

# We produce a signal with multiple frequency components
# x(n) = [ series of 10 random integers elem {0..10} ]
#
size = 10
x = np.random.randint(10, size=size)

# Sample axis
n = np.array(range(size)) + 1

## Plot the signal

timeFig = plt.figure()

plt.stem(n, x, basefmt=' ')

plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid(True)
plt.show(block=False)

## DTFT

# Frequency axis
w = np.arange(0, 2 * math.pi, 0.05)

#
# NOTE
# The DTFT function `freqz` can only output a sampled spectrum. However,
# we are using a frequency axis which is quite dense. For this purpose,
# we can consider the ouptut of `freqz` as continuous.
#
_, X_dtft = freqz(x, 1, len(w), whole=True)

spectrumFig = plt.figure()

# Amplitude spectrum
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(X_dtft), color='blue')

# Formatting the plot
plt.xlim(0, 2 * math.pi)
plt.xticks(np.linspace(0, 2 * math.pi, 5), ['0', '$\\pi$/2', '$\\pi$', '3$\\pi$/2', '2$\\pi$'])
plt.grid(True)
plt.xlabel('$\\Omega$')
plt.ylabel('|X($\\Omega$)|')

# Phase spectrum
plt.subplot(2, 1, 2)
plt.plot(w, np.angle(X_dtft), color='blue')

# Formatting the plot
plt.xlim(0, 2 * math.pi)
plt.xticks(np.linspace(0, 2 * math.pi, 5), ['0', '$\\pi$/2', '$\\pi$', '3$\\pi$/2', '2$\\pi$'])
plt.ylim(-math.pi, math.pi)
plt.yticks(np.linspace(-math.pi, math.pi, 5), ['-$\\pi$', '-$\\pi$/2', '0', '$\\pi$/2', '$\\pi$'])
plt.grid(True)
plt.xlabel('$\\Omega$')
plt.ylabel('angle(X($\\Omega$))')

plt.show()

input("Example 01 complete.")
