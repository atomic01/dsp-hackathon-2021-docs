# ***************************************
#        Basic Modulations example
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Basic level example of QAM4 modulation


#------------------------------------------------
# Define used libraries
#------------------------------------------------
from numpy import exp, pi, absolute, arange, reshape, random, array, round, zeros
import math
from spectrum01 import spectrum01
import matplotlib.pyplot as plt

# ==========================================================
# Parameters
# ==========================================================
M = 4 # QAM 4 modulation
R = random.rand(1, 1024) 
b = round(R[0])
b = b.astype(int) # 1024 randomly generated bits

f0=10 # Carrier frequency [Hz]
TSimbola=0.3 # Symbol duration [s]
fSample=1000 # Sampling frequency
tSample=1/fSample # Sampling period

Ns=int(round(TSimbola/tSample)) # Number of samples per one symbol
BBS=int(math.log2(M)) # Number of bits per one symbol
L=len(b); # Number of bits to be transmitted

# Symbol forming
Sb=b.reshape(BBS,int(L/BBS)); # Every column one symbol
Ss = [0] * len(Sb[0])
# Convert every two bits to a number [0,3]
for i in range(len(Sb[0])):
    Ss[i]=2 * Sb[0][i] + Sb[1][i]

# ==========================================================
# Mapping symbols to constellation
# ==========================================================
Constellation=[1+1j, -1+1j, 1-1j, -1-1j] #Symbol map definition
Ac  = zeros((1,len(Ss)), dtype=complex)

# Searching the map
for i in range(len(Ss)):   
    index = int(Ss[i])
    Ac[0][i]=Constellation[index]

plt.figure(1)
plt.plot(Ac.real,Ac.imag,'.')
plt.title('Constellation')
plt.xlabel('Real')
plt.ylabel('Imag')

# ==========================================================
# Modulation
# ==========================================================
t=arange(Ns)*tSample
uQAM = []
Signal_ks = zeros((len(t),), dtype=complex)
C = exp(-1j*2*pi*f0*t) # Complex signal carrier
E = Ac[0]

# Generating the signal
for ks in range(len(E)): 
    for i in range(Ns):
        Signal_ks[i]=E[ks] * C[i]   # Multiplying by complex carrier
    uQAM.extend(Signal_ks.real) # Appending the current symbol to the end of the signal

plt.figure(2)
plt.plot(uQAM[:2000]) # Zoom in to see the waveform
plt.title('QAM signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# ==========================================================
# Spectrum 
# ==========================================================
plt.figure(3)
spectrum01(uQAM,fSample)
plt.title('QAM Signal spectrum')
plt.show()
