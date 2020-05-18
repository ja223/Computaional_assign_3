#Question 5
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
import time
def DFT(q,func_arr):# Definition of the DFT for a particular q
    N = len(func_arr)
    F = 0
    for n in range(N):
         F += func_arr[n] * np.exp(- 2j *np.pi * q * n / N)
    return F/(np.sqrt(N))
p=0
time_DFT=np.zeros(97)
time_numpy=np.zeros(97)
for n in range(4,101):   # as n goes from 4 to 100 there are 97 n value     
    sampled_arr=np.arange(n)# sample data 
    DFT_direct=np.zeros(n, dtype=np.complex)
    start_time1=time.time()
    for i in range(n):
        DFT_direct[i]=DFT(i, sampled_arr)
    time_DFT[p]=time.time()-start_time1 # time required for not using numpy
    start_time2=time.time()
    DFT_numpy=np.fft.fft(sampled_arr)
    time_numpy[p]=time.time()-start_time2# time required for using numpy
    p=p+1
x=np.linspace(4,100,97)
plt.xlabel('n')
plt.ylabel('Time_required')
plt.plot(x,time_DFT, '.-', color='b', label='Time taken without using numpy.fft')
plt.plot(x,time_numpy, 'g--', label='Time taken using numpy.fft' )
plt.title(' comparison between DFT method and numpy.fft')
plt.legend()
plt.show()
