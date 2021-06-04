# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:10:39 2021

@author: PC
"""

import matplotlib.pyplot as plt

beta = 0.185
alpha = 0.022
nP = 51049498

fs = lambda s,i: -beta*s*i/nP
fi = lambda s,i: -fs(s,i) - alpha*i
fr = lambda i: alpha*i

i = [3015301,3031726]
r = [2835554,2848153]
s = [nP - i[0] + r[0],nP - i[1] + r[1]]

for k in range(21):
    s.append(s[-1] + (1.5*fs(s[-1],i[-1]) - 0.5*fs(s[-2],i[-2])))
    i.append(i[-1] + (1.5*fi(s[-2],i[-1]) - 0.5*fi(s[-3],i[-2])))
    r.append(r[-1] + (1.5*fr(i[-2]) - 0.5*fr(i[-3])))
    
    print("Dia ",k + 1,": {:.5f},{:.5f},{:.5f}".format(s[k],i[k],r[k]))
d = [3015301,3031726,3048719,3067879,3084460,3103333,3118426,3131410,3144547,3161126,3177212,3192050,3210787,3232456,3249433,3270614,3294101,3319193,3342567,3363061,3383279,3406456]


plt.plot(range(len(s)),s,"r")
plt.plot(range(len(i)),i,"b")
plt.plot(range(len(r)),r,"g")
plt.plot(range(len(d)),d,"m")
plt.show()