# *********************************************
# Aliasing in spectral domain - grating lobes
# *********************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# We observe the effect of aliasing, which occurs when the line source
# distance is larger than \lambda/2. In that case the spectral images from
# discretization come into visible region and grating lobes would occur at
# some angles. The "safest" direction from aliasing is the broadside one 
# and it tolerates the distances of up to \lambda.

# In this example we fix the array total length to 6*\lambda.We reduce the
# number of elements from 12 (Nyquist distance \lambda/2) to 8 and 4 and
# observe how the grating lobe arrives into visible region.

# Importing relevant modules
import math
import numpy as np

import matplotlib.pyplot as plt
from scipy import special

# Normalized wavenumber space
# We take range -3:3 so that both visible and invisible ranges are seen
#beta_z/beta = cos(theta)
beta_n=np.linspace(-3,3,num=1201) 

#Setting the array parameters...

L=6 #total array length (normalized to wavelength)
N=np.array([12,8,4]) #numbers of antenna elements
d=np.divide(L,N)# distance between antennas
d1=d [:,np.newaxis]*beta_n*2*np.pi # Auxiliary variable (factor 2*pi is due to normalization!)


#Initialization of array factor fields...
AF = [[None for i in beta_n] for j in d]
AF_dB = [[None for i in beta_n] for j in d]
#The normalized array factor is taken in closed form (Dirichlet function):
for x in range(len(d)):
 AF[x] =special.diric (d1[x],N[x])

AF_dB=20*np.log10(np.abs(AF))

# We plot the array factors for observed cases separately to ensure
# visibility

#plotting case without aliasing
plt.figure(1)
p1=plt.plot(beta_n, AF_dB[0])
plt.legend(['d=0.5 $\lambda$ - no aliasing'])
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

#plotting case with aliasing but not "strong" enough to bring grating lobe
plt.figure(2)
p1=plt.plot(beta_n, AF_dB[1])
plt.legend(['d=0.75 $\lambda$ - aliasing but no visible grating lobes'])
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


#plotting case with aliasing and grating lobe in visible region
plt.figure(3)
p1=plt.plot(beta_n, AF_dB[2])
plt.legend(['d=1.5 $\lambda$ - aliasing & visible grating lobes'])
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
theta=np.arccos(beta_v) #Transformation from spectral to angular domain

# Now we plot array factor in polar graph - again separately for each case

# Plotting case without aliasing
fig = plt.figure(4)
ax = fig.add_subplot(111, projection='polar')
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ticks = np.linspace(0, np.pi, 7)
ax.set_xticks(ticks)
ax.set_rlim(-30,0)
plt.plot(theta,AFdB_v [0])
plt.legend(['d=0.5 $\lambda$ - no aliasing'])
plt.title ('Normalized array factor in angular (theta) domain')
plt.ylabel('Relative level [dB]')


# Plotting case with aliasing but not "strong" enough to bring grating lobe
fig = plt.figure(5)
ax = fig.add_subplot(111, projection='polar')
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ticks = np.linspace(0, np.pi, 7)
ax.set_xticks(ticks)
ax.set_rlim(-30,0)
plt.plot(theta,AFdB_v [1])
plt.legend(['d=0.75 $\lambda$ - aliasing but no visible grating lobes'])
plt.title ('Normalized array factor in angular (theta) domain')
plt.ylabel('Relative level [dB]')


# Plotting case with aliasing and grating lobe in visible region
fig = plt.figure(6)
ax = fig.add_subplot(111, projection='polar')
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ticks = np.linspace(0, np.pi, 7)
ax.set_xticks(ticks)
ax.set_rlim(-30,0)
plt.plot(theta,AFdB_v [2])
plt.legend(['d=1.5 $\lambda$ - aliasing & visible grating lobes'])
plt.title ('Normalized array factor in angular (theta) domain')
plt.ylabel('Relative level [dB]')

plt.show()