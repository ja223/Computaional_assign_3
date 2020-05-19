/*Question 2
Jagannath Das(DTP)(PhD)*/
#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
void main()
{       
        int i, numpoints=256;
        float x_min=-50.0, x_max=50.0, delta=(x_max-x_min)/(numpoints-1), xarr[numpoints], freq, ft_real, ft_imag;
	fftw_complex* sam_data;
	fftw_complex* answer;	
        sam_data = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * numpoints); /*allocating memory for sample data and fourier data*/
	answer = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * numpoints);
        //Define the sinc function.
        i=0;
	while ( i < numpoints)
	{
		sam_data[i][1] =0;
		if ((x_min+delta*i)!=0)
		  	sam_data[i][0] = sin(x_min+delta*i)/(x_min+delta*i);
		else
			sam_data[i][0] =1;
	        i++;
	}
        fftw_plan p;
	p = fftw_plan_dft_1d(numpoints, sam_data, answer, FFTW_FORWARD, FFTW_ESTIMATE);/*definition of DFT using FFTW*/
        fftw_execute(p);
        FILE *Fourier;
    	Fourier=fopen("num2.txt","w"); /*opening  a file in  write mode*/
        i=0;
	while (i<numpoints)
  	{
	   if (i<=numpoints/2-1)
	   {
		freq=(2*M_PI/(numpoints*delta))*(i);
	   }
	   else
	   {
		freq=(2*M_PI/(numpoints*delta))*(i-numpoints); /*setting up array of k values */
	   }
	   ft_real=(1/sqrt(numpoints))*answer[i][0]; 
   	   ft_imag=(1/sqrt(numpoints))*answer[i][1];
	   ft_real= delta*sqrt(numpoints/(2*M_PI))*(cos(freq*x_min)*ft_real+sin(freq*x_min)*ft_imag);/*Definition of fourier transform using discrete fourier transform*/
	   ft_imag= delta*sqrt(numpoints/(2*M_PI))*(cos(freq*x_min)*ft_imag-sin(freq*x_min)*ft_real);
	   fprintf(Fourier,"%e\t%e\n",freq,ft_real);
	   
           i++;
	}
	
	fclose(Fourier);	

	fftw_destroy_plan(p);
}
