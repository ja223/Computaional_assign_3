#Question 8
#Jagannath Das(DTP)(PhD)
import numpy as np 
import matplotlib.pyplot as plt 
def f(x):#Definition of the function given
    if -1<x<1:
        value=1
    else:
        value=0
    return value
def DFT(func_arr):# Definition of discrete fourier transform
    N = len(func_arr)
    Fourier_arr = []
    for m in range(N):
        F = 0
        for n in range(N):
            F += func_arr[n] * np.exp(- 2j *np.pi * m * n / N)
        Fourier_arr.append(F / (np.sqrt(N)))
    return Fourier_arr
def IDFT(func_arr):# Definition of inverse discrete fourier transform
    N = len(func_arr)
    IFourier_arr = []
    for m in range(N):
        F = 0
        for n in range(N):
            F += func_arr[n] * np.exp(+ 2j *np.pi * m * n / N)
        IFourier_arr.append(F / (np.sqrt(N)))
    return IFourier_arr
x_min = -5.0 #minimum value of x
x_max = 5.0#maximum value of x
numpoints = 256#number of smple points
delta = (x_max-x_min)/(numpoints-1)# resolution
sampled_arr = np.zeros(numpoints)
x_arr = np.zeros(numpoints)
for i in range(numpoints):
        sampled_arr[i] = f(x_min+i*delta)
        x_arr[i] = x_min+i*delta

nft = DFT(sampled_arr)#discrete fourier transform
karr = 2*np.pi*np.fft.fftfreq(numpoints, d=delta)#k points
odr=karr.argsort()[::1]# sorting of the k points 
Double=np.asarray(nft)*np.asarray(nft)# np.asarray allows to multiply an array with a non-integer in python
Func_x=delta*np.sqrt(256)*np.asarray(IDFT(Double))# definition of the convolution 
Func_x=Func_x[odr]
plt.plot(x_arr,np.real(Func_x),'b',label='Convolution of the Box function to it-self')
plt.plot(x_arr,sampled_arr,'r', label='The box function')
plt.xlabel('x',fontsize=16)
plt.ylabel('f(x)',fontsize=16)
plt.grid(True)
plt.legend()
plt.show()


