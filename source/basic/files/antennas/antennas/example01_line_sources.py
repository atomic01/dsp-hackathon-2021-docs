# ***************************************
#  Spatial factor of a line source
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 

# Here we observe how the length of line source of length L affects the
# beamwidth (and hence spatial resolution).
#
# Broadside sources (uniform magnitude) are assumed here. We observe lengths of 2, 5 and 10
# lambdas but one can play with them further...

# Importing relevant modules
import math
import numpy as np

import matplotlib.pyplot as plt
from scipy import special

## Define a line source and find its radiation pattern ("space factor")

# Normalized wavenumber space
# We take range -3:3 so that both visible and invisible ranges are seen
#beta_z/beta = cos(theta)
beta_n=np.linspace(-3,3,num=1201) 

#Normalized source length in units of lambda...
L=np.array([2,5,10]) 

d1=L[:,np.newaxis]*beta_n*2*np.pi #Auxiliary variable (factor 2*pi is due to normalization!)

#Initialization of space factor fields...
SF = [[None for i in beta_n] for j in L]
SF_dB = [[None for i in beta_n] for j in L]
#The normalized array factor is taken in closed form (Dirichlet function):
for x in range(len(L)):
 SF[x] =special.sinc(d1[x]/(2*np.pi))

SF_dB=20*np.log10(np.abs(SF))

# Plot the spatial factor in spectral (beta_z) domain ...

plt.figure(1)
p1=plt.plot(beta_n, SF_dB[0], label= r'$L=2*\lambda$')
p2=plt.plot(beta_n, SF_dB[1], label= r'$L=5*\lambda$')
p3=plt.plot(beta_n, SF_dB[2], label= r'$L=10*\lambda$')
plt.legend()
plt.axvline(x=-1,color='red',linestyle='--',label='Visible range boundary')
plt.axvline(x=1,color='red',linestyle='--',label='Visible range boundary')
plt.text(-0.9,-20,"Visible region boundary",rotation=90,color='red')
plt.text(0.8,-20,"Visible region boundary",rotation=90,color='red')
plt.xlim(min(beta_n), max(beta_n))
plt.ylim(-30, 0)
plt.grid()
plt.title ('Normalized pattern in spectral domain - line source')
plt.xlabel(r'$\beta_z/\beta=cos(\theta)$')
plt.ylabel('Relative level [dB]')

##Extracting the visible region for generation of polar plot
v_min = (np. where(beta_n == -1))[0][0]
v_max = (np. where(beta_n == 1))[0][0]
beta_v=beta_n[v_min:v_max]
SFdB_v=SF_dB[:,v_min:v_max]
theta=np.arccos(beta_v) #Transformation from spectral to angular (\theta) domain

# Now we plot space factor (pattern) in polar graph - i.e. in angular domain

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='polar')
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ticks = np.linspace(0, np.pi, 7)
ax.set_xticks(ticks)
ax.set_rlim(-30,0)
p4=plt.plot(theta, SFdB_v[0], label= r'$L=2*\lambda$')
p5=plt.plot(theta, SFdB_v[1], label= r'$L=5*\lambda$')
p6=plt.plot(theta, SFdB_v[2], label= r'$L=10*\lambda$')
leg=plt.legend()
plt.title ('Normalized pattern in angular domain (theta-plane)')
plt.ylabel('Relative level [dB]')

plt.show()