#Question 2 second part
#Jagannath Das(DTP)(PhD)
import numpy as np 
import matplotlib.pyplot as plt 
def f(x):#Definition of the function
    if x !=0:
        value=(1/x)*np.sin(x)
    else:
        value=1
    return value
x_min = -50.0 #minimum value of x
x_max = 50.0#maximum value of x
numpoints = 256 #number of smple points
delta = (x_max-x_min)/(numpoints-1)# resolution
sampled_arr = np.zeros(numpoints)
x_ar = np.zeros(numpoints)
for i in range(numpoints):
        sampled_arr[i] = f(x_min+i*delta)
        x_ar[i] = x_min+i*delta
nft = np.fft.fft(sampled_arr, norm='ortho') #discrete fourier transform using numpy
karr = np.fft.fftfreq(numpoints, d=delta)# set of k points 
karr = 2*np.pi*karr
factor = np.exp(-1j * karr * x_min)
aft = delta * np.sqrt(numpoints/(2.0*np.pi)) * factor * nft # Definition of fourier transform fron discrete fourier trnsform

fou=open("num2.txt","r")           #Read the data obtained from Q_2_1.c
Sampled_data=fou.readlines()
i=0
numpoints=np.size(Sampled_data)
x_arr=np.zeros(numpoints)
func_x=np.zeros(numpoints)
for D in Sampled_data:
    Data_1,Data_2=D.split()
    x_arr[i]=float(Data_1)
    func_x[i]=float(Data_2)
    i=i+1
plt.subplot(1,2,1)
plt.plot(x_arr,func_x,'g',label = 'Fourier transform of given Function by FFTW')
plt.xlabel('k',fontsize=16)
plt.ylabel('f_FFTW(k)',fontsize=16)
plt.legend()
plt.grid(True)


plt.subplot(1,2,2)
plt.plot(karr,aft,'b',label = 'Fourier transform of given Function by numpy')
plt.xlabel('k',fontsize=15)
plt.ylabel('f_numpy(k)',fontsize=15)
plt.legend()
plt.show()

