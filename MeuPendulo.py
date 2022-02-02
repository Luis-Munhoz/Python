# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 08:33:35 2022

@author: Luís Fernando
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits import mplot3d

#rc('font', **{'family':'sans-serif','sans-serif':['Helvetica']})
#rc('text', usetex=True)

time0 = time.time()

#%% Parâmetros de simulação:
Fs = 100      # Frequência de amostragem [Hz]
dt = 0.01     # Taxa de amostragem [s]
nd = 3        # Número de equações diferenciais (estados)
N = 10000       # Número de pontos

X_rk4 = np.zeros((nd, N))
t_rk4 = np.zeros(N)
Tv = []
Nv = []

#%% Parâmetros do modelo:
g = 9.81        # [m/s^2]
m = 0.1           # [kg]
L = 0.25        # [m]
R = 0.5         # [m]   
phi_p = 0.5     # [rad/s]
H = 0.5         # [m]
r=0.2
l=0.1

#%% Conjunto de equações diferenciais:
def __dXdt__( Xd ):  
    theta = Xd[0]
    p1 = r*np.cos(theta)*phi_p**2/l
    p2 = np.sin(theta)*np.cos(theta)*phi_p**2
    p3 = -g*np.sin(theta)/l
    
    # Matriz A:
    A = np.array([  [                 0,      1,       0       ], \
                    [  (p1+p2+p3)/theta,      0,       0       ], \
                    [                 0,      0,   phi_p/Xd[2] ] ]) 
    
    # Solução:
    sol = A.dot(Xd) 

    return sol
    
#%% Integradores numéricos: 
# Condições iniciais:
theta0 = 45*np.pi/180
omega0 = 0
phi0 = 1*np.pi/180
X_rk4[:,0] = [theta0, omega0, phi0]

#%% Loop:
for k in range(0, N-1):
    print('Iteração número: ' + str(k))
    kk1 = __dXdt__( X_rk4[:,k] )
    kk2 = __dXdt__( X_rk4[:,k] + kk1*(dt/2) )
    kk3 = __dXdt__( X_rk4[:,k] + kk2*(dt/2) )
    kk4 = __dXdt__( X_rk4[:,k] + kk3*dt )
    X_rk4[:,k+1] = X_rk4[:,k] + (dt/6)*(kk1 + 2*kk2 + 2*kk3 + kk4)
    t_rk4[k+1] = t_rk4[k] + dt
                              
elapsed = time.time() - time0
elp = elapsed/60
print("Elapsed time: %f.2 [mins]" % elp)

theta_v = X_rk4[0,:]
omega_v = X_rk4[1,:]
phi_v = X_rk4[2,:]


#%% Cinemática:
plt.figure(1)
plt.subplot(211)
plt.plot(t_rk4, theta_v, 'b', linewidth=2, label='$RK4$')
plt.ylabel(r'$\theta(t)$ $[^{o}]$', fontsize=20)
plt.xlim(t_rk4[0], t_rk4[-1])
plt.ylim(-1,1)
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=20)

plt.subplot(212)
plt.plot(t_rk4, omega_v, 'k', linewidth=2, label='$RK4$')
plt.xlabel('$t$ $[s]$', fontsize=20)
plt.ylabel(r'$\omega(t)$ $[^{o}/s]$', fontsize=20)
plt.ylim(-5,5)
plt.xlim(t_rk4[0], t_rk4[-1])
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=20)

#%% Trajetória:
fig = plt.figure()
ax = plt.axes(projection='3d')
#EQUAÇÕES DO ROB NAS SUAS RESPECTIVAS BASES
# Inercial:
xc_I = np.cos(phi_v)*(l*np.sin(theta_v)+r)
yc_I = -l*np.cos(theta_v)
zc_I =  -np.sin(phi_v)*(l*np.sin(theta_v)+r)

# Móvel B1:
xc_B1 =   l*np.sin(theta_v)+r
yc_B1 =  -l*np.cos(theta_v)
zc_B1 =  np.zeros(N)

# Móvel B2:
xc_B2 =  r*np.cos(theta_v)
yc_B2 =  -l-r*np.sin(theta_v)
zc_B2 = np.zeros(N)

plt.figure(2)
ax.plot3D(xc_I,yc_I,zc_I, 'b')
ax.set_xlabel(r'$x_{I}$ $[m]$', fontsize=15)
ax.set_ylabel(r'$y_{I}$ $[m]$', fontsize=15) 
ax.set_zlabel(r'$z_{I}$ $[m]$', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.show()

#%% Reações:
#EQUAÇÕES OBTIDOS PELA F=MA E T=IH
Nz = m*(-2*np.cos(theta_v)*theta_v*phi_v*l)
Ty = (m*((theta_v**2)*l+np.sin(theta_v)*r*(phi_v**2)+(np.sin(theta_v)**2)*l*(phi_v**2)))+m*g*np.cos(theta_v)

plt.figure(3)
plt.subplot(211)
plt.plot(t_rk4, Nz, 'b')
plt.ylabel(r'$N_{x}(t)$', fontsize=20)
plt.xlim(t_rk4[0], t_rk4[-1])
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=20)

plt.subplot(212)
plt.plot(t_rk4, Ty, 'b')
plt.xlabel('$t$ $[s]$', fontsize=20)
plt.ylabel(r'$T_{z}(t)$', fontsize=20)
plt.xlim(t_rk4[0], t_rk4[-1])
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=20)