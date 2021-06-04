# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 01:16:44 2021

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def df_dt(x, t, a, b, c, d):
    dx = a * x[0] - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    return np.array([dx, dy])

a = 0.4 #razon de crecimiento de las presas
b = 0.37 #razon de interaccion de depredadores y presas 
c = 0.3 #razon de muerte de depredadores 
d = 0.05
# Condiciones iniciales
x0 = 3   # Presas
y0 = 1  # Depredadores
conds_iniciales = np.array([x0, y0])
tf = 200
N = 800
t = np.linspace(0, tf, N)
solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))


plt.plot(t, solucion[:, 0], label='presa')
plt.plot(t, solucion[:, 1], label='depredador')