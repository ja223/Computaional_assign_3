#Question 1
#Jagannath Das(DTP)(PhD)
import numpy as np 
import matplotlib.pyplot as plt 
def f(x):#Definition of the function
    if x !=0:
        value=(1/x)*np.sin(x)
    else:
        value=1
    return value
def g(x):#Definition of the analytical fourier transform
    if -1<x<1:
        val=np.sqrt((np.pi)/2)
    else:
        val=0
    return val
x_min = -50.0 #minimum value of x
x_max = 50.0#maximum value of x
numpoints = 256 #number of smple points
delta = (x_max-x_min)/(numpoints-1)# resolution
sampled_arr = np.zeros(numpoints)
x_arr = np.zeros(numpoints)
for i in range(numpoints):
        sampled_arr[i] = f(x_min+i*delta)
        x_arr[i] = x_min+i*delta
nft = np.fft.fft(sampled_arr, norm='ortho') #discrete fourier transform using numpy
karr = np.fft.fftfreq(numpoints, d=delta)# set of k points 
karr = 2*np.pi*karr
factor = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(numpoints/(2.0*np.pi)) * factor * nft # Definition of fourier transform fron discrete fourier trnsform
k_min=-8.0
k=np.zeros(161)
F_analy=np.zeros(161)
for j in range(161):
       F_analy[j] = g(k_min+j*0.1)
       k[j] = k_min+j*0.1

plt.xlabel('k')
plt.ylabel('fourier_f(k)')
plt.plot(k,F_analy,color = 'c',label = 'Fourier transform of given Function analytically')
plt.plot(karr,aft,color = 'r',label = 'Fourier transform of given Function by numpy')
plt.title('DFT method for sinc function')
plt.legend()
plt.grid()
plt.show()

