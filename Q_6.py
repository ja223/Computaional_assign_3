#Question 6
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
def DFT(func_arr):# Definition of the DFT
    N = len(func_arr)
    Fourier_arr = []
    for m in range(N):
        F = 0
        for n in range(N):
            F += func_arr[n] * np.exp(- 2j *np.pi * m * n / N)
        Fourier_arr.append(F / (np.sqrt(N)))
    return Fourier_arr
x_min = -10.0 #minimum value of x
x_max = 10.0#maximum value of x
numpoints = 256 #number of smple points
delta = (x_max-x_min)/(numpoints-1)# resolution
func_arr = np.zeros(numpoints)
x_arr = np.zeros(numpoints)
for i in range(numpoints):
        func_arr[i] = 1#constant function  is assumed to be 1
        x_arr[i] = x_min+i*delta
nft =  DFT(func_arr)# Discrete fourier transform of the function
karr =2*np.pi* np.fft.fftfreq(numpoints, d=delta)# k points 
factor = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(numpoints/(2.0*np.pi)) * factor * nft # Definition of fourier transform fron discrete fourier trnsform
fig=plt.figure()
plt.subplot(2,2,1)
plt.plot(x_arr,func_arr,'b',label='The constant function ')
plt.title('The constant function')
plt.xlabel('x',fontsize=16)
plt.ylabel('func_x',fontsize=16)

plt.grid(True)

plt.subplot(2,2,2)
plt.plot(karr,aft,'b', label='The fourier transform of the constant function')
plt.title('The fourier transform of the constant function')
plt.xlabel('k',fontsize=16)
plt.ylabel('Fourier_f',fontsize=16)
plt.grid(True)
plt.show()



