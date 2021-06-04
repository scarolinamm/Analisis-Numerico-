# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 22:56:48 2021

@author: PC
"""

import numpy as np 
import pylab as plt

beta = 0.185
N = 51049498

miu = 0.022

tsim = 21
step = 21
h = tsim/step


S = np.zeros([step + 1,1])
I = np.zeros([step + 1,1])


t = np.linspace(0,tsim,step+1)

I[0] = 3015301
S[0] = N-I[0] 

for i in range(step):
    F = np.array([[-beta * S[i] * I[i]/N],[beta * S[i] * I[i]/N ]], dtype = 'float')
    
    S[i+1] = S[i] + h * F[0]
    I[i+1] = I[i] + h * F[1]
    print("dia: ",i," infectados:",I[i], " suceptibles: ", S[i])

    
D = np.array([3015301,3031726,3048719,3067879,3084460,3103333,3118426,3131410,3144547,3161126,3177212,3192050,3210787,3232456,3249433,3270614,3294101,3319193,3342567,3363061,3383279,3406456])

plt.xlim(0,21)
plt.ylim(2500000,5000000)
plt.plot(t,S, label = 'Suceptibles')
plt.plot(t,I, label = 'Infectados')
plt.plot(t,D, label = 'Datos reales')
plt.title("Modelo SI")
plt.xlabel('Dias')
plt.ylabel('Numero de personas')
plt.legend()