#!/usr/bin/python

# ***************************************
#          Downsampling example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021

import sys
import numpy as np
import matplotlib.pyplot as plot
from scipy import signal
import array as arr

#********************************************************************************************
#Downsampling - aliasing

#create band-limited input signal
f = arr.array('d', [0, 0.2500, 0.5000, 0.7500, 1.0000])
a = arr.array('d', [1.00, 0.6667, 0.3333, 0.0, 0.0])

nf = 512
b1 = signal.firwin2(nf - 1, f, a)
w, h = signal.freqz(b1, 1, nf)
omega = np.arange(-np.pi, np.pi - 2*np.pi/nf, 2*np.pi/nf)

#create decimated signal
#y = signal.decimate(b1, 2, zero_phase=True)             #decimate does antialias filtering
y = signal.resample(b1, len(b1)//2)
w, hy = signal.freqz(y, 1, nf)

#plot spectrums of input and decimated signal and observe the aliasing
plot.plot(omega/np.pi, np.absolute(h), 'b')
plot.plot(omega/np.pi, np.absolute(hy), 'r')
plot.xlabel('pi rad/s')
plot.ylabel('Magnitude')
plot.suptitle('Input vs Decimated signal (aliasing)')
plot.show()
#********************************************************************************************
#Downsampling - decimate

f1 = 1          #frequency of first component in signal
f2 = 2          #frequency of second component in signal
R = 4           #decimation factor
fs1 = 50        #sampling frequency of the input signal
fs2 = fs1/R     #sampling frequeny of the decimated signal
Nx = 50

#create an input signal
nx = np.arange(Nx - 1)
x = np.sin(2*np.pi*(f1/fs1)*nx) + np.sin(2*np.pi*f2/fs1*nx)

#creat a decimated signal
y = signal.resample(x, len(x)//R)
ny = np.arange(len(y))

#plot input and decimated signal in time domain
fig, (ax1, ax2) = plot.subplots(1, 2)
fig.suptitle('Time domain')

ax1.stem(nx,x)
ax1.set_xlabel('n')
ax1.set_ylabel('x[n]')
ax1.title.set_text('Input signal')

ax2.stem(ny,y, 'r')
ax2.set_xlabel('n')
ax2.set_ylabel('y[n]')
ax2.title.set_text('Decimated signal')
plot.show()

Nfft = 256
fk1 = np.fft.fftfreq(Nfft, 1/fs1)
X = np.fft.fft(x, Nfft)

fk2 = np.fft.fftfreq(Nfft, 1/fs2)
Y = np.fft.fft(y, Nfft)

#plot amplitude spectrums of input and decimated signals
fig, (ax1, ax2) = plot.subplots(1, 2)
fig.suptitle('Amplitude spectrum')

ax1.plot(fk1, 20*np.log10(np.abs(X)))
ax1.set_xlabel('f[Hz]')
ax1.set_ylabel('Amplitude [dB]')
ax1.title.set_text('Input signal')

ax2.plot(fk2, 20*np.log10(np.abs(Y)), 'r')
ax2.set_xlabel('f[Hz]')
ax2.set_ylabel('Amplitude [dB]')
ax2.title.set_text('Decimated signal')
plot.show()
