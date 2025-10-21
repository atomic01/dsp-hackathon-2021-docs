#!/usr/bin/python

# ***************************************
#          Multirate example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021

import sys
import numpy as np
import matplotlib.pyplot as plot
from scipy import signal
import array as arr

#********************************************************************************************
#Upsampling

f = arr.array('d', [0, 0.2500, 0.5000, 0.7500, 1.0000])
a = arr.array('d', [1.00, 0.5000, 0.0, 0.0, 0.0])

nf = 512
b1 = signal.firwin2(nf - 1, f, a)
w, h = signal.freqz(b1, 1, nf)
omega = np.arange(-np.pi, np.pi - 2*np.pi/nf, 2*np.pi/nf)

#create interpolated signal
y = signal.resample(b1, len(b1)*2)
w, hy = signal.freqz(y, 1, nf)

#plot both signals in frequency domain - shrunk spectrum
#no alias images can be observed due to antialias filtering in the resample method
plot.plot(omega/np.pi, np.absolute(h), 'b')
plot.plot(omega/np.pi, np.absolute(hy), 'r')
plot.xlabel('pi rad/s')
plot.ylabel('Magnitude')
plot.suptitle('Input vs Upsampled signal')
plot.show()

#********************************************************************************************
#Upsampling - interpolating with zeros

N = 40
L = 3
fs1 = 10
fs2 = L*fs1
f0 = 3
tx = np.arange(N/fs1)

#input signal
x = np.cos(2*np.pi*f0*tx)

#interpolated signal with "manually" added zeroes in between samples to show the imaging effect
y = np.zeros(3*len(x))
y[::3] = x

#y = signal.resample(x, len(x)*L)
ty = np.arange(len(y))

#plot input and interpolated signal in time domain
Nfft = 256
fig, (ax1, ax2) = plot.subplots(1, 2)
fig.suptitle('Input vs Interpolated signal (time domain)')

ax1.stem(tx,x)
ax1.set_xlabel('n')
ax1.set_ylabel('x[n]')
ax1.title.set_text('Input signal')

ax2.stem(ty,y)
ax2.set_xlabel('n')
ax2.set_ylabel('y[n]')
ax2.title.set_text('Interpolated signal')
plot.show()

Nfft = 256
fk1 = np.fft.fftfreq(Nfft, 1/fs1)
X = np.fft.fft(x, Nfft)

fk2 = np.fft.fftfreq(Nfft, 1/fs2)
Y = np.fft.fft(y, Nfft)

#plot amplitude spectrums of input and decimated signals
fig, (ax1, ax2) = plot.subplots(1, 2)
fig.suptitle('Amplitude spectrum')

ax1.plot(fk1, 20*np.log10(np.abs(X), out=np.abs(X), where=np.abs(X)>0))
ax1.set_xlabel('f[Hz]')
ax1.set_ylabel('Amplitude [dB]')
ax1.title.set_text('Input signal')

ax2.plot(fk2, 20*np.log10(np.abs(Y), out=np.abs(Y), where=np.abs(Y)>0))
ax2.plot(fk2, 20*np.log10(np.abs(Y)), 'r')
ax2.set_xlabel('f[Hz]')
ax2.set_ylabel('Amplitude [dB]')
ax2.title.set_text('Interpolated signal')
plot.show()

#observe that the amplitude spectrum of the interpolated signal is shrunk and images of the original signal are occurring
