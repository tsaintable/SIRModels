import scipy.integrate as spi
import numpy as np
import pylab as pl

beta=1.4247
gamma=0.14286
I0=1e-6
ND=70
TS=1.0
INPUT = (1.0-I0, I0)

def SIS(x,t):  
	'''The main set of equations'''
	Y=np.zeros((2))
	X = x    
	Y[0] = - beta * X[0] * X[1] + gamma * X[1]
	Y[1] = beta * X[0] * X[1] - gamma * X[1]
	return Y   # For odeint



t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

print(RES)

#Ploting
pl.subplot(211)
pl.plot(RES[:,0], '-g', label='Susceptibles')
pl.title('Program_2_5.py')
pl.xlabel('Time')
pl.ylabel('Susceptibles')
pl.subplot(212)
pl.plot(RES[:,1], '-r', label='Infectious')
pl.xlabel('Time')
pl.ylabel('Infectious')
pl.show()