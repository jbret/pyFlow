import numpy as np
import matplotlib.pyplot as plt
import time, sys

# step 4, In 7

def linearconv(nx):
    Lx = 2.
    dx = Lx / (nx-1)
    nt = 20
    c = 1.     # wave speed
    sigma = .5

    dt = sigma * dx

    u = np.ones(nx)
    u[int(.5/dx):int(1./dx+1)] = 2.

    un = np.ones(nx)   # temp array

    for n in range(nt):
        un = u.copy()
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

    plt.plot(np.linspace(0,Lx,nx), u); plt.show()

#linearconv(121)

def lineardiffuse(nx):
    Lx = 2.
    dx = Lx / (nx-1)
    nt = 20
    nu = .3
    sigma = .2
    dt = sigma * dx**2 / nu

    u = np.ones(nx)
    u[int(.5/dx):int(1./dx+1)] = 2.

    un = np.ones(nx)   # temp array

    for n in range(nt):
        un = u.copy()
        for i in range(1, nx-1):
            u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])

    plt.plot(np.linspace(0,Lx,nx), u); plt.show()

lineardiffuse(41)


