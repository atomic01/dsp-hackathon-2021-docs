# ***************************************
#           OFDM tx example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Basic level example for OFDM tx simbol generation
#

import math
import numpy as np

import matplotlib.pyplot as plt

from scipy.fft import fft

# 0. Message (bitstream) creation 

# in this example, we will use OAM-16 modulation for coding the subcarriers
# in OFDM simbol
# note difference between "simbol" and "OFDM simbol"
# simbol is part of tx message, in this case carrying 4 bit length information (possible values 0-15)
# Each simbol is coded into amplitude and phase of specific OFDM subcarrier
# Together specific number of OFDM subcarriers make OFDM simbol 

simbolsTx=np.array((8, 9, 12, 12, 3, 2, 9, 8, 13, 8, 4, 8, 4, 2, 0, 11, 9, 8, 3, 7, 3, 7, 11, 0, 10, 12, 15, 0, 14, 14, 3, 15, 8, 3, 3, 7, 15, 2, 2, 0, 10, 2, 3, 4, 3, 9, 2, 4, 7, 0, 8, 6, 8, 10, 1, 12, 1, 1, 15, 9, 5, 15, 6, 4, 13, 9, 0, 13, 0, 12, 0, 8, 6, 4, 8, 7, 14, 0, 5, 3, 3, 3, 1, 5, 9, 3, 7, 4, 14, 13, 1, 6,  14, 1, 14, 14, 4, 0, 15, 9, 4, 9, 8, 4, 8, 13, 15, 13, 0, 3, 15, 7, 4, 9, 14, 6, 7, 0, 15, 14, 7, 0, 9, 6, 11, 10, 1, 6, 0, 2, 12, 2, 7, 5, 5, 7, 15, 11, 15, 2, 0, 11, 3, 5, 4, 6, 13, 3, 2, 13, 10, 3, 10, 0, 11, 15, 11, 15, 12, 3, 0, 8))
# 1. OFDM parameters  

# total 256 OFDM bins
Nfft=256 # total number of OFDM sub-carriers 
Ng=Nfft/4 # length of guard interval
fs=30.72e6; #sampling frequency of the system 

#frequency axis for FFT, as range [-fs/2,fs/2]
deltaf=fs/Nfft
f=np.fft.fftfreq(Nfft,1/fs)
f=np.fft.fftshift(f)

# positions [-103,-102,...,0,...,102,103] are used
activeSubcarriersPos=np.arange(-103,104,1) 

# pilot positions [-103,-98,...,-3,...,3,8,...,103] 
pilotSubcarriersPos=np.concatenate((np.arange(-103,0,5), np.arange(3,104,5)))
pilotAmplitude=1
pilotPhase=0
# DC subcarriers
subCarriersAroundDcPos=np.array([-1,0,1])

# position of data subcarriers are the rest of active subcarrier positions, that are not pilot or DC positions
dataSubcarriersPos=activeSubcarriersPos[np.isin(activeSubcarriersPos,np.concatenate((pilotSubcarriersPos,subCarriersAroundDcPos)), invert=True)]

# 2. Simbols mapping 

constellation = np.array(
[ 1+1j,   # 0='0000'#
  1+3j,   # 1='0001'
  3+1j,   # 2='0010'
  3+3j,   # 3='0011'
  1-1j,   # 4='0100'
  1-3j,   # 5='0101'
  3-1j,   # 6='0110'
  3-3j,   # 7='0111'
  -1+1j,  # 8='1000'
  -1+3j,  # 9='1001'
  -3+1j,  #10='1010'
  -3+3j,  #11='1011'
  -1-1j,  #12='1100'
  -1-3j,  #13='1101'
  -3-1j,  #14='1110'
  -3-3j,  #15='1111'
  ])

Aph_dataSubcarriers=constellation[(simbolsTx)]

# 3. Create OFDM simbol
OFDMsimbol_f=np.zeros(Nfft,dtype = 'complex_')
indexOffset=Nfft/2

# first place pilot subcarriers
pilotIndices=pilotSubcarriersPos+indexOffset
OFDMsimbol_f[pilotIndices.astype(int)]=pilotAmplitude*np.exp(1j*pilotPhase)

# then place data subcarriers
dataIndices=dataSubcarriersPos+indexOffset
OFDMsimbol_f[dataIndices.astype(int)]=Aph_dataSubcarriers

# Plot amplitude and phase spectrum of OFDM simbol
ofdmSimbolFig = plt.figure()
plt.subplot(2,1,1);
plt.stem(f/1e6, np.abs(OFDMsimbol_f))
plt.title('OFDM simbol - amplitude spectrum');
plt.xlabel('f [MHz]');
plt.ylabel('Amplitude');
plt.subplot(2,1,2);
plt.stem(f/1e6, np.angle(OFDMsimbol_f)*180/np.pi)
plt.title('OFDM simbol - phase spectrum');
plt.xlabel('f [MHz]');
plt.ylabel('Phase [deg]');

# 4. Perform IFFT modulation and add Cylcic prefix 
OFDMsimbol_t=np.fft.ifft(np.fft.ifftshift(OFDMsimbol_f), Nfft)

# add cyclic prefix
cp=OFDMsimbol_t[np.arange(Nfft-Ng, Nfft,dtype = 'int')] 
OFDMsimbol_t=np.concatenate((cp,OFDMsimbol_t)); 

It=np.real(OFDMsimbol_t); # in-phase component sent in time domain
Qt=np.imag(OFDMsimbol_t); # quadrature-phase component sent in time domain

t=np.arange(0,Nfft+Ng)/fs;

iqSamplesFig = plt.figure()
plt.subplot(2,1,1);
plt.plot(t*10e6, It);
plt.title('OFDM in-phase component I(t)');
plt.xlabel('$t[\mu s]$');
plt.ylabel('Amplitude [db]');
plt.subplot(2,1,2);
plt.plot(t*10e6, Qt);
plt.title('OFDM quad-phase component Q(t)');
plt.xlabel('$t[\mu s]$');
plt.ylabel('Phase [deg]');

plt.show()