# ***************************************
# Planar array - array factor
# ***************************************
# Ericsson Nikola Tesla
# DSP Hackaton 2021
# 
# We have seen that with linear arrays we can steer the beam in one plane
# only. With planar arrays we can achieve full 3D scan. We show the example
# of planar array with rectangular grid which acts as a product of two
# linear arrays in x- and y-direction.  We calculate the two 1D (linear)
# array factors in spectral domain and take their product to obtain 2D
# array factor (we choose distances of lambda/2 to remain within Nyquist criterion).

# Importing relevant modules
import math
from matplotlib.colors import Colormap
import numpy as np

import matplotlib.pyplot as plt
from scipy import special

# Normalized wavenumber space
# We take range -3:3 so that both visible and invisible ranges are seen
#beta_z/beta = cos(theta)
betax_n=np.linspace(-3,3,num=1201) 
betay_n=np.linspace(-3,3,num=1201) 

#creating 2D wavenumber space (for plotting the surf plot)
XX,YY=np.meshgrid(betax_n,betay_n)

#Setting the array parameters in x- and y- direction

dx=0.5 #normalized distance in wavelength (in x-direction)
dy=0.5  #normalized distance in wavelength (in y-direction)
M=10  #Number of antenna elements in X
N=5  #Number of antenna elements in Y

# Setting desired angles of maximum for beam steering(we choose broadside direction)
#This gives us beamforming capability

theta_0=0 # In this coordinates broadside appears at \theta=0!
phi_0=90 #This becomes interesting when we move from broadside

#Calculating required linear phase shift rates both in x- and y-direction(normalized to beta)

alphax_n=-np.sin(np.deg2rad(theta_0))*np.cos(np.deg2rad(phi_0))
alphay_n=-np.sin(np.deg2rad(theta_0))*np.sin(np.deg2rad(phi_0))

psix_n=XX*dx+alphax_n*dx; #auxiliary angles for array factor calculations (in X)
psiy_n=YY*dy+alphay_n*dy; #auxiliary angles for array factor calculations (in Y)

d1_x=psix_n*2*np.pi #Auxiliary variable in x 
d1_y=psiy_n*2*np.pi #Auxiliary variable in y (factor 2*pi is due to normalization...)

#The normalized array factor is taken in closed form (Dirichlet function):
# Array factor in X...
AFx =special.diric (d1_x,M)  #normalized array factor of array 
AFx_dB=20*np.log10(np.abs(AFx))

AFy =special.diric (d1_y,N)  #normalized array factor of array
AFy_dB=20*np.log10(np.abs(AFy))

# Plotting array factors in spectral domains (beta_x and beta_y) separately

#Linear array factor in x-direction
plt.figure(1)
p1=plt.plot(betax_n, AFx_dB[0,:])
plt.axvline(x=-1,color='red',linestyle='--',label='Visible range boundary')
plt.axvline(x=1,color='red',linestyle='--',label='Visible range boundary')
plt.text(-0.9,-20,"Visible region boundary",rotation=90,color='red')
plt.text(0.8,-20,"Visible region boundary",rotation=90,color='red')
plt.xlim(min(betax_n), max(betax_n))
plt.ylim(-30, 0)
plt.grid()
plt.title ('X-direction - spectral domain')
plt.xlabel(r'$\beta_x/\beta=sin(\theta)\cdot cos(\phi)$')
plt.ylabel('Relative level [dB]')

#Linear array factor  in y-direction
plt.figure(2)
p2=plt.plot(betay_n, AFy_dB[:,0])
plt.axvline(x=-1,color='red',linestyle='--',label='Visible range boundary')
plt.axvline(x=1,color='red',linestyle='--',label='Visible range boundary')
plt.text(-0.9,-20,"Visible region boundary",rotation=90,color='red')
plt.text(0.8,-20,"Visible region boundary",rotation=90,color='red')
plt.xlim(min(betay_n), max(betay_n))
plt.ylim(-30, 0)
plt.grid()
plt.title ('Y-direction - spectral domain')
plt.xlabel(r'$\beta_y/\beta=sin(\theta)\cdot sin(\phi)$')
plt.ylabel('Relative level [dB]')

#Calculation of 2D spectral domain array factor as a product of two linear array factors...
AF_tot=AFx*AFy
AFtot_dB=20*np.log10(np.abs(AF_tot))
np.clip(AFtot_dB,-40,0,out=AFtot_dB) #clipping the unnecessary data below -40 dB

#Parameters of unit circle which defines visible region in 2D case
th=np.linspace (0,2*np.pi,1001)
x=np.cos(th)
y=np.sin(th)

# plotting the array factor in 2D spectral domain (beta_x beta_y)..
plt.figure(3)
p3= plt.contourf(XX,YY,AFtot_dB,cmap=plt.cm.bone)
#Adding unit circle as a visible region boundary
p3a=plt.plot(x,y,color='red',linestyle='--',label='Visible range' )
#Setting other plot parameters
plt.text(-1,1.2,"Visible region",rotation=0,color='red')
plt.gca().set_aspect("equal")
cbar = plt.colorbar()
cbar.set_label('Relative level [dB]', rotation=90)
plt.title ('Planar array - 2D spectral domain')
plt.xlabel(r'$\beta_x/\beta=sin(\theta)\cdot cos(\phi)$')
plt.ylabel(r'$\beta_y/\beta=sin(\theta)\cdot sin(\phi)$')

plt.show()