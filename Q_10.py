#Question 10
#Jagannath Das(DTP)(PhD)
import numpy as np 
import matplotlib.pyplot as plt 
def DFT(func_arr):
    N = len(func_arr)
    Fourier_arr = []
    for m in range(N):
        F = 0
        for n in range(N):
            F += func_arr[n] * np.exp(- 2j *np.pi * m * n / N)
        Fourier_arr.append(F / (np.sqrt(N)))
    return Fourier_arr
fou=open("noise.txt","r")           #Read the data obtained from link given in the question
Sampled_data=fou.readlines()
i=0
numpoints=np.size(Sampled_data)
x_arr=np.zeros(numpoints)
func_x=np.zeros(numpoints)
for i in range(numpoints):
     x_arr[i]=i
     func_x[i]=Sampled_data[i]
Fou_arr = DFT(func_x) # discrete fourier transform
k_arr = 2*np.pi*np.fft.fftfreq(numpoints, d=1)
power_arr=np.zeros(numpoints)
Power_Spec=np.zeros(numpoints)
i=0
while (i<numpoints):
      Power_Spec[i]=(1/numpoints)*np.absolute(Fou_arr[i])*np.absolute(Fou_arr[i]) #power spectrum using periodogram
      i=i+1
K_arr=int((max(k_arr)-min(k_arr)))
bins=10
width=K_arr/bins
lower_bound=min(k_arr)
upper_bound=max(k_arr)

K1=np.linspace(lower_bound,upper_bound,bins+1)
Power_bin=np.zeros(bins)
K_bin=np.zeros(bins)
for i in range(bins):# Definition of Power_spectrum with binned frequency
	count=0
	for j in range(len(k_arr)):
		if K1[i]<=k_arr[j]<K1[i+1]:
			Power_bin[i]+=Power_Spec[j]
			count+=1
	Power_bin[i]=Power_bin[i]/count	
	K_bin[i]=K1[i]+(K1[i+1]-K1[i])/2
fig1,ax1 =plt.subplots()
ax1.plot(x_arr,func_x,'b')
ax1.set_title('Plotting of the measurements vs time(say)')
ax1.set_xlabel('time',fontsize=15)
ax1.set_ylabel('Measurements',fontsize=15)

fig2,ax2 =plt.subplots()
ax2.plot(k_arr,Fou_arr,'b')
ax2.set_title('Plotting of fourier transform of the measurements vs freqency(say)')
ax2.set_xlabel('frequency',fontsize=16)
ax2.set_ylabel('Fourier_measurements',fontsize=16)

fig3,ax3 =plt.subplots()
ax3.plot(k_arr,Power_Spec,'b',label='Plotting of power spectrum')
ax3.set_title('Plotting of power spectrum')
ax3.set_xlabel('frequency',fontsize=16)
ax3.set_ylabel('Power_spectrum',fontsize=16)

fig4,ax4 =plt.subplots()
ax4.bar(K_bin,Power_bin,width) 
ax4.set_title('Plotting of binned power spectrum')
ax4.set_xlabel('binned Frequency',fontsize=16)
ax4.set_ylabel('binned power_spectrum',fontsize=16)

plt.grid(True)
plt.show()

