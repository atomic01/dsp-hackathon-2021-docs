# Calculates the spectrum of input signal by performing FFT
# Specify 1 as fs to plot a spectrum of digital signal

from scipy.fft import fft, fftshift
from numpy import linspace
import numpy as np
import math
import matplotlib.pyplot as plt

def spectrum01(x,fs):
    N=len(x)
    Nfft=10*N
    X = fftshift(fft(x,Nfft))
    X=X/N
    m = np.max(np.abs(X))
    X = X/m
    f=fos(Nfft,fs)
    X=[20*np.log10(np.abs(x)) for x in X]
    plt.plot(f,X)
    plt.ylabel('Spectrum [dB/(\Delta Hz)]')
    plt.xlabel('Frequency[Hz]')
    plt.ylim(-100, 0)

    return

# Calculates the frequency axis for the spectral samples obtained by FFT
def fos( N, fs ):

    if (N <= 0) : 
        print('Number of samples must be a positive number greater than 0')


    if (fs <= 0) : 
        print('Number of samples must be a positive number greater than 0')

    deltaf = fs/N

    if (N%2==0 ) :  # even N
        f = linspace(-fs/2,fs/2-deltaf, num = N)
    else : # odd N
        f = linspace(-(fs-deltaf)/2,(fs-deltaf)/2,num = N)

    return f