/*Question 4
Jagannath Das(DTP)(PhD)*/
#include <stdio.h>    
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#define x_max 50.0 /* maximum value of x */
#define x_min -50.0 /* minimum value of x*/
#define numpoints 256 /* number of data points*/
void sample_data (fftw_complex* func ,double delta) /* Defining the sample data */
{
  int i;
  double x;
  i=0;
  while (i<numpoints)
  {
    x=x_min+i*delta;		
    func[i][0]=exp(-pow(x,2)); 
    func[i][1]=0;
    i++;
  }
}
int main()
{       
	fftw_complex* sam_data;
	fftw_complex* answer;	/*setting up  arrays to store sample data and fourier data*/
	double freq,delta=(x_max-x_min)/(numpoints-1),ft_real,ft_imag;
        sam_data = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * numpoints); /*allocating memory for sample data and fourier data*/
	answer = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * numpoints);
	fftw_plan p;
	p = fftw_plan_dft_1d(numpoints, sam_data, answer, FFTW_FORWARD, FFTW_ESTIMATE);/*definition of DFT using FFTW*/
        sample_data(sam_data,delta);
        fftw_execute(p);
        FILE *Fourier;
    	Fourier=fopen("num4.txt","w"); /*opening  a file in  write mode*/
	int i;
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
