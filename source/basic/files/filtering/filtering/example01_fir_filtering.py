# ***************************************
#       Basic filtering example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Example of basic filtering;
# Extracting 3 frequency components out of a discretes dignal

#------------------------------------------------
# Define used libraries
#------------------------------------------------
from numpy import sin, pi, absolute, arange, convolve
from scipy.signal import remez
from spectrum01 import spectrum01
import matplotlib.pyplot as plt

N = 1000 # number of samples
n = arange(N) # samples of a discretised signal 

fs = 1000 # [Hz] sampling frequency
f1 = 10 # [Hz] (digital frequency 0.01)
f2 = 100 # [Hz] (digital frequency 0.1)
f3 = 200 # [Hz] (digital frequency 0.2)

x1 = sin(2*pi*f1/fs*n)
x2 = sin(2*pi*f2/fs*n)
x3 = sin(2*pi*f3/fs*n)

x = x1 + x2 + x3 # creating the signal 

plt.figure(1)
plt.plot(n, x, linewidth=1)
plt.title('Original signal')

plt.figure(2)
spectrum01(x,1) # Spectrum of dicrete signals is periodical with period 1 
plt.title('Original signal spectrum')

#------------------------------------------------
# LOW-PASS filter
#------------------------------------------------
# Designing the low-pass filter
freq1 = [0, 0.05, 0.15, 1]
freq1 = [fc / 2 for fc in freq1]
amp1 = [1, 0]
f1 = remez(99,freq1,amp1, fs=1)

plt.figure(3)
spectrum01(x,1)
spectrum01(f1,1)
plt.title('Frequency response of low-pass filter')

# Filtering by convolution
y1 = convolve(x,f1)

plt.figure(4)
plt.plot(x1)
plt.plot(y1)
plt.title('Extracted low-pass component of the signal')

#------------------------------------------------
# BAND-PASS filter
#------------------------------------------------
# Designing the band-pass filter
freq2 = [0, 0.1, 0.2, 0.3, 0.4, 1]
freq2 = [fc / 2 for fc in freq2]
amp2 = [0, 1, 0]
f2 = remez(99,freq2,amp2, fs=1)

plt.figure(5)
spectrum01(x,1)
spectrum01(f2,1)
plt.title('Frequency response of band-pass filter')

# Filtering by convolution
y2 = convolve(x,f2)

plt.figure(6)
plt.plot(x2)
plt.plot(y2)
plt.title('Extracted band-pass component of the signal')


#------------------------------------------------
# HIGH-PASS filter
#------------------------------------------------
# Designing the high-pass filter
freq3 = [0, 0.2, 0.4, 1]
freq3 = [fc / 2 for fc in freq3]
amp3 = [0, 1]
f3 = remez(99,freq3,amp3, fs=1)

plt.figure(7)
spectrum01(x,1)
spectrum01(f3,1)
plt.title('Frequency response of high-pass filter')

# Filtering by convolution
y3 = convolve(x,f3)

plt.figure(8)
plt.plot(x3)
plt.plot(y3)
plt.title('Extracted high-pass component of the signal')

plt.show()








