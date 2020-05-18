#Question 8
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
numpoints=64 # no of data points 
x_min,x_max=-50,50 # maximum and minimum value of x
y_min,y_max=-50,50# maximum ans minimum value of y
x_arr = np.zeros(numpoints)
y_arr = np.zeros(numpoints)
sampled_x_arr = np.zeros(numpoints)
sampled_y_arr = np.zeros(numpoints)
delta_x=(x_max-x_min)/(numpoints-1)#resolution of x
delta_y=(y_max-y_min)/(numpoints-1)# resolution of y
for i in range(numpoints):
        y_arr[i]= y_min+i*delta_y
        x_arr[i] = x_min+i*delta_x
x_arr,y_arr = np.meshgrid(x_arr, y_arr)
z_arr=np.exp(-x_arr**2-y_arr**2)        #Given function
Kx_arr = 2*np.pi*np.fft.fftfreq(numpoints,d=delta_x) #k points corresponding to x
Ky_arr = 2*np.pi*np.fft.fftfreq(numpoints,d=delta_y)# k points corresponding to y
kx_arr,ky_arr = np.meshgrid(Kx_arr, Ky_arr)# meshgrid returns co-ordinate matrixs from co-ordinate vectors
func=np.fft.fft2(z_arr,norm="ortho") # 2D fourier tranform from numpy
factor=np.exp(-1j*kx_arr*x_min)*np.exp(-1j*ky_arr*y_min)
F_arr=delta_x*delta_y*factor*(numpoints/(2.0*np.pi))*func# definition of fourier transform from discrete fourier transform
fig=plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(kx_arr,ky_arr,np.real(F_arr),cmap=cm.cool) # 3D plot of fourier tranfrom form numpy
ax1.set_title('3D plot of fourier tranfrom from numpy')
ax1.set_xlabel('kx',fontsize=14)
ax1.set_ylabel('ky',fontsize=14)
ax1.set_zlabel('Fourier_numpy',fontsize=14)
ax2 = fig.add_subplot(122, projection='3d')
kx_arr,ky_arr = np.meshgrid(Kx_arr, Ky_arr)
g_arr=0.5*np.exp(0.25*(-kx_arr**2-ky_arr**2))#Analytical solution of the fourier transform
ax2.plot_surface(kx_arr,ky_arr,g_arr,cmap=cm.hot) # 3D plot of fourier tranfrom analytically
ax2.set_title('3D plot of fourier tranfrom analytically')
ax2.set_xlabel('kx',fontsize=14)
ax2.set_ylabel('ky',fontsize=14)
ax2.set_zlabel('Fourier_analy',fontsize=14)
plt.show()


