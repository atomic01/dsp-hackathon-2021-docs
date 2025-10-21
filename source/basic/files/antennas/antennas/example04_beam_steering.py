# ***************************************
#  Linear phase shift - beam steering
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Here we observe the effect of adding the progressive phase shift \alpha*d
# along the array. Within visible region we will see how the spectrum 
#(i.e. the array factor) moves along normalized beta_z axis. The array is
# discretized with distance of \lambda/2 (Nyquist criterion)


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

d=0.5 #normalized distance in wavelength
N=20 #Number of antenna elements
L=N*d #total array length
theta_0=np.array([120,90,45]) #desired angles of maximum radiation (in degrees)
alpha_n=-np.cos(np.deg2rad(theta_0)) #required linear phase shift rate (normalized to beta)
psi_n=beta_n*d+alpha_n[:,np.newaxis]*d #Auxiliary angle \psi
d1=psi_n*2*np.pi #Auxiliary variable (factor 2*pi is due to normalization!)...


#Initialization of array factor fields...
AF = [[None for i in beta_n] for j in theta_0]
AF_dB = [[None for i in beta_n] for j in theta_0]
#The normalized array factor is taken in closed form (Dirichlet function):
for x in range(len(theta_0)):
 AF[x] =special.diric (d1[x],N)

AF_dB=20*np.log10(np.abs(AF))

# We plot the array factors for observed cases separately to ensure
# visibility

#plotting case without aliasing
plt.figure(1)
p1=plt.plot(beta_n, AF_dB[0], label= r'$\theta_0$=120 deg.')
p2=plt.plot(beta_n, AF_dB[1], label= r'$\theta_0$=90 deg.')
p3=plt.plot(beta_n, AF_dB[2], label= r'$\theta_0$=45 deg.')
leg=plt.legend()
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

# Extracting the visible region for generation of polar plot
v_min = (np. where(beta_n == -1))[0][0]
v_max = (np. where(beta_n == 1))[0][0]
beta_v=beta_n[v_min:v_max]
AFdB_v=AF_dB[:,v_min:v_max]
theta=np.arccos(beta_v) #Transformation from spectral to angular (\theta) domain

# Now we plot array factor (visible range) in polar graph 

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='polar')
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ticks = np.linspace(0, np.pi, 7)
ax.set_xticks(ticks)
ax.set_rlim(-30,0)
p4=plt.plot(theta, AFdB_v[0], label= r'$\theta_0$=120 deg.')
p5=plt.plot(theta, AFdB_v[1], label= r'$\theta_0$=90 deg.')
p6=plt.plot(theta, AFdB_v[2], label= r'$\theta_0$=45 deg.')
leg=plt.legend()
plt.title ('Normalized array factor in angular (theta) domain')
plt.ylabel('Relative level [dB]')

plt.show()