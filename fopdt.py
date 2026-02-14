import numpy as np

def fopdt(t, theta, tau):
    return 1 - np.exp(-(t - theta) / tau)

def fopdt_k(k, t, theta, tau):
    return k * fopdt(t, theta, tau)
