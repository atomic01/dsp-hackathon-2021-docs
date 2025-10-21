# ***************************************
#           Mixing example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Basic level example of real and complex mixer in digital domain (NCO)
#

import math
import numpy as np

import matplotlib.pyplot as plt

from scipy.fft import fft

# 1. Generate input cosine signal with little bit of noise and plot the amplitude spectrum
fs=1024 #sampling frequency 
N=1024 #number of samples of sine signal 
t=np.arange(0,N-1)/fs
f0=32; #signal frequency

x = np.cos(2 * np.pi * f0 * t)
noise = np.random.normal(0, .1, x.shape)
x = x + noise

## Plot the time domain signal
inputSignalFig = plt.figure();

plt.stem(t,x)
plt.xlabel("time[s]")
plt.ylabel("")
plt.title("Input signal")

#Plot the spectrum
Nfft=256
deltaf=fs/Nfft
f=np.fft.fftfreq(Nfft,1/fs)
f=np.fft.fftshift(f) #frequency axis for FFT, as range [-fs/2,fs/2]

X=np.fft.fft(x,Nfft)
X=np.fft.fftshift(X)

inputSpectrumFig = plt.figure()
plt.plot(f,20*np.log10(np.abs(X)))
plt.xlabel("f[Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Amplitude spectrum - input signal")

# 2. Do the frequency upconversion with real mixer, fNCO=128Hz

fNCO=128
xNCO=np.cos(2*np.pi*fNCO*t)
xout1=np.multiply(xNCO,x);
Xout1=np.fft.fftshift(np.fft.fft(xout1,Nfft));

realUpconversionFig = plt.figure()
plt.plot(f,20*np.log10(np.abs(Xout1)))
plt.xlabel("f[Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Amplitude spectrum - real mixer upconversion")

# with real mixer, 4 spectral components will appear after the upconversion
# a) fNCO+f0 ->  this one we usually need for further processing
# b) fNCO-f0
# c) -fNCO-f0
# d) -fNCO+f0

# 3. Do the frequency upconversion with complex mixer, fNCO=128Hz
fNCO=128;
xNCO=np.exp(1j*2*np.pi*fNCO*t);
xout2=np.multiply(xNCO,x);
Xout2=np.fft.fftshift(np.fft.fft(xout2,Nfft));

cmplxUpconversionFig = plt.figure()
plt.plot(f,20*np.log10(np.abs(Xout2)))
plt.xlabel("f[Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Amplitude spectrum - complex mixer upconversion")

# with complex mixer, 2 spectral components will appear after the upconversion
# a) fNCO+f0 ->  this one we usually need for further processing
# b) fNCO-f0

# 4. Do the frequency downconversion with complex mixer, fNCO=-256Hz
fNCO=-256;
xNCO=np.exp(1j*2*np.pi*fNCO*t);
xout3=np.multiply(xNCO,x);
Xout3=np.fft.fftshift(np.fft.fft(xout3,Nfft));

cmplxUpconversionFig = plt.figure()
plt.plot(f,20*np.log10(np.abs(Xout3)))
plt.xlabel("f[Hz]")
plt.ylabel("Amplitude [dB]")
plt.title("Amplitude spectrum - complex mixer downconversion")

# with complex mixer, 2 spectral components will appear after the upconversion
# a) fNCO+f0 ->  this one we usually need for further processing
# b) fNCO-f0

plt.show()
