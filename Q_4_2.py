#Question 4
#Jagannath Das(DTP)(PhD)
import numpy as np 
import matplotlib.pyplot as plt 
def g(x):#Definition of the analytical fourier transform
    return 0.5*np.exp(-0.25*x**2)
x_min = -10.0 #minimum value of x
x_max = 10.0#maximum value of x
numpoints = 256 #number of smple points
delta = (x_max-x_min)/(numpoints-1)# resolution
x_ar=np.zeros(numpoints)
F_analy=np.zeros(numpoints)
for j in range(numpoints):
       x_ar[j]=x_min+j*delta
       F_analy[j] = g(x_min+j*delta)

fou=open("num4.txt","r")           #Read the data obtained from Q_2_1.c
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
plt.plot(x_ar,F_analy,'b',label = 'Fourier transform of given Function by analytically')
plt.xlabel('k',fontsize=15)
plt.ylabel('f_analy(k)',fontsize=15)
plt.legend()
plt.grid(True)
plt.show()

