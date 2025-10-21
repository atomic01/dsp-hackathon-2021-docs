# ***************************************
#  Discretization of line source
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
#

# The total length of line source
# when discretized would correspond to total array length (L=N*d). If
# discretized by Nyquist criterium, we would also see that in visible region
# the array factor corresponds to the space factor of the line source.

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

#Discretizing line source with N samples within Nyquist criterion...
N=np.array([4,10,20]) #numbers of antenna elements

d=np.divide(L,N) #Fixed distance of \lambda/2

d1=d[:,np.newaxis]*beta_n*2*np.pi #Auxiliary variable (factor 2*pi is due to normalization!)

#Initialization of space factor fields...
AF = [[None for i in beta_n] for j in L]
AF_dB = [[None for i in beta_n] for j in L]

#The normalized array factor is taken in closed form (Dirichlet function):
for x in range(len(d)):
 AF[x] =special.diric (d1[x],N[x])

AF_dB=20*np.log10(np.abs(AF))

# Plot the spatial factor in spectral (beta_z) domain ...

plt.figure(1)
p1=plt.plot(beta_n, AF_dB[0], label= 'N=4')
p2=plt.plot(beta_n, AF_dB[1], label= 'N=10')
p3=plt.plot(beta_n, AF_dB[2], label= 'N=20')
plt.legend()
plt.axvline(x=-1,color='red',linestyle='--',label='Visible range boundary')
plt.axvline(x=1,color='red',linestyle='--',label='Visible range boundary')
plt.text(-0.9,-20,"Visible region boundary",rotation=90,color='red')
plt.text(0.8,-20,"Visible region boundary",rotation=90,color='red')
plt.xlim(min(beta_n), max(beta_n))
plt.ylim(-30, 0)
plt.grid()
plt.title ('Normalized array factor in spectral domain')
plt.xlabel(r'$\beta_z/\beta=cos(\theta)$')
plt.ylabel('Relative level [dB]')

##Extracting the visible region for generation of polar plot
v_min = (np. where(beta_n == -1))[0][0]
v_max = (np. where(beta_n == 1))[0][0]
beta_v=beta_n[v_min:v_max]
AFdB_v=AF_dB[:,v_min:v_max]
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
p4=plt.plot(theta, AFdB_v[0], label= 'N=4')
p5=plt.plot(theta, AFdB_v[1], label= 'N=10')
p6=plt.plot(theta, AFdB_v[2], label= 'N=20')
leg=plt.legend()
plt.title ('Normalized array factor in angular (theta) domain')
plt.ylabel('Relative level [dB]')

plt.show()