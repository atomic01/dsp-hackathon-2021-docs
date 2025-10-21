# ***************************************
# Multibeam generation and analysis
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# Want to radiate multiple beams? No problem. Due to linearity one can at
# the same time apply multiple current distributions with different linear
# phases giving rise to different beams at the same time (it is good to have
# a large enough array to have enough spatial resolution and to remain 
# within Nyquist criterion). 

# Note that this multibeam does not arise from aliasing but from the design
# of proper current distributions...

# This example shows how to generate beams at 60 and 120 degrees.The array
# factor and required current magnitudes are calculated and plotted.

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
theta_0=np.array([120,60]) #desired angles of maximum radiation (in degrees)
alpha_n=-np.cos(np.deg2rad(theta_0)) #required linear phase shift rate (normalized to beta)
psi_n=beta_n*d+alpha_n[:,np.newaxis]*d #Auxiliary angle \psi
d1=psi_n*2*np.pi #Auxiliary variable (factor 2*pi is due to normalization!)

#Initialization of array factor fields...
AF = [0 for i in range(len(beta_n))]
#AF_dB = [[None for i in beta_n] for j in theta_0]
#The normalized array factor is taken in closed form (Dirichlet function):
for x in range(len(theta_0)):
 AF+=special.diric (d1[x],N)

AF_dB=20*np.log10(np.abs(AF))

# We plot the array factors for observed cases separately to ensure
# visibility

#plotting case without aliasing
plt.figure(1)
p1=plt.plot(beta_n, AF_dB, label= 'Beams at cos (theta) =+-1/2')
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

##Extracting the visible region for generation of polar plot
v_min = (np. where(beta_n == -1))[0][0]
v_max = (np. where(beta_n == 1))[0][0]
beta_v=beta_n[v_min:v_max]
AFdB_v=AF_dB[v_min:v_max]
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
p4=plt.plot(theta, AFdB_v, label= 'Beams at angles theta of 60 and 120 deg.')
leg=plt.legend()
plt.title ('Normalized array factor in angular (theta) domain')
plt.ylabel('Relative level [dB]')

# Calculation of current distribution at each antenna
# We need to sum contributions from each beam (total current is not uniform
# anymore)

I = [0 for i in range(N)]
M=len(alpha_n)

for k in range(N):
    for m in range (M):
        I[k]+=np.exp(-1j*k*d*alpha_n[m])

plt.figure(3)
plt.subplot(2,1,1)
plt.stem(np.abs(I/max(I)))
plt.title('Beam indices - magnitudes')
plt.grid()
plt.xticks([0,4,9,14,19],[1,5,10,15,20])
plt.xlabel('Antenna element number')
plt.ylabel('Normalized current magnitude')

plt.subplot(2,1,2)
plt.stem(np.rad2deg(np.angle(I)))
plt.title('Beam indices - phases')
plt.xticks([0,4,9,14,19],[1,5,10,15,20])
plt.grid()
plt.xlabel('Antenna element number')
plt.ylabel('Current phase')
plt.subplots_adjust(hspace=0.8)

plt.show()