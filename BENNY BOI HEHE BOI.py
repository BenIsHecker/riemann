#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install matplotlib')


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
#The next library contains the zeta(), zetazero(), and siegelz() functions
from mpmath import *
mp.dps = 25; mp.pretty = True

def graph_zeta(real, image_name):
    A,B,C = [], [], []

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in np.arange(0.1, 60.0, 0.1):
        function = zeta(real + 1j*i)
        function1 = siegelz(i)
        A.append(abs(function))
        B.append(function1)
        C.append(i)

    ax.grid(True)
    ax.plot(C,A, label='modulus of Riemann zeta function along critical line, s = 1/2 + it', lw=0.8)
    ax.plot(C,B, label='Riemann-Siegel Z-function, Z(t)', lw=0.8)
    ax.set_title("Riemann Zeta function - re(s)=1/2")
    ax.set_ylabel("Z(t)")
    ax.set_xlabel("t")

    #Include legend
    leg = ax.legend(shadow=True)
    #Edit font size of legend to make it fit into chart
    for t in leg.get_texts():
        t.set_fontsize('small')
    #Edit the line width in the legend
    for l in leg.get_lines():
        l.set_linewidth(2.0)
    #Plot the zeroes of zeta
    for i in xrange(1, 13):
        zero = zetazero(i)
        ax.plot(zero.imag, [0.0], "ro")
    
    #save plot and print that it was saved 
    ax.set_ylim(-7, 7)
    plt.savefig(image_name)
    print ("Successfully plotted %s !" % image_name)
    plt.close()


graph_zeta(0.5, "Z(t)_Plot.png")


# In[5]:


https://hub.gke2.mybinder.org/user/ipython-ipython-in-depth-180186ma/notebooks/binder/Untitled.ipynb?kernel_name=python3
    


# In[7]:


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpmath import zeta, zetazero

def calc_zeta(re, img_name):
    X,Y,Z = [], [], []

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in np.arange(0.1, 50.0, 0.1):
        compl = zeta(complex(re, i))
        X.append(compl.real)
        Y.append(compl.imag)
        Z.append(i)

    ax.grid(True)
    ax.plot(Z,X, label='Im(v)', lw=0.8)
    ax.plot(Z,Y, label='Re(v)', lw=0.8)
    ax.set_title("Riemann Zeta function - re(s)=%.3f" % re)
    ax.set_xlabel("Im(s)")
    ax.set_ylabel("Re(v) and Im(v)")

    leg = ax.legend(shadow=True)   
    for t in leg.get_texts():
        t.set_fontsize('small')

    for l in leg.get_lines():
        l.set_linewidth(2.0)

    # Plot the zeroes of zeta
    for i in xrange(1, 11):
        zero = zetazero(i)
        ax.plot(zero.imag, [0.0], "ro")

    # Comment this line for autoscale
    ax.set_ylim(12, -12)
    plt.savefig(img_name)
    print ("Plot %s !" % img_name)
    plt.close()

if __name__ == "__main__":
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    file_index = 0
    for i in np.arange(0.01, 10.0, 0.01):
        file_index += 1
        calc_zeta(i, "zeta_plot1_%s.png" % file_index)


# In[ ]:

if_name_ == "_main_"
    try:prin(2.292019291083757107299297475872810828429083804765777728389298)
        prin(2.928183828394829578901082084088290928282827274658738392828201)
        prin(1.282819372795671082827173972908104001028382923898274972902081)


