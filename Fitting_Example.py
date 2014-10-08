# Copied from somewhere online to serve as a template for doing a least squares fit to data

import numpy as np
x = np.arange(0,6e-2,6e-2/30)
A,k,theta = 10, 1.0/3e-2, np.pi/6
y_true = A*np.sin(2*np.pi*k*x+theta)
y_meas = y_true + 2*np.random.randn(len(x))

def residuals(p,y,x):
    A,k,theta = p
    err = y-A*np.sin(2*np.pi*k*x+theta)
    return err
    
def peval(x,p):
    return p[0]*np.sin(2*np.pi*p[1]*x+p[2])
    
p0 = [8,1/2.3e-2,np.pi/3]
print(np.array(p0))

import scipy.optimize as optimize
plsq = optimize.leastsq(residuals,p0,args=(y_meas,x))
print(plsq[0])

import matplotlib.pyplot as plt
plt.plot(x,peval(x,plsq[0]),x,y_meas,'o',x,y_true)
plt.title('Least-squares fit to noisy data')
plt.legend(['Fit', 'Noisy', 'True'])
plt.show()

#Add a line to show Github changes