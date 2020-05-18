/*Question 2
Jagannath Das(DTP)(PhD)*/
/* similar python coding needed as Q_2_2.py to show  plot except the name of the text file*/
#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define real(z,i) ((z)[2*(i)])
#define img(z,i) ((z)[2*(i)+1])

int main (void)
{
	int n=128,i;
	double data[2*n],a=-10,b=10,delx=(b-a)/(n-1),k[n],fk[n];

	//Define the sinc function.
	for (i = 0; i < n; i++)
	{
		img(data,i) =0;
		if ((a+delx*i)!=0)
		  	real(data,i) = sin(a+delx*i)/(a+delx*i);
		else
			real(data,i) =1;
	}

	for (i = 0; i < n; i++)
	{
	   k[i]=-M_PI/delx+i/(n*delx)*2*M_PI;
	}

	gsl_fft_complex_radix2_forward (data, 1, n);

	FILE *out;
	out = fopen("q3.txt","w");

	
	for (i = 0; i <= n/2; i++)				
	{
		fk[i+n/2-1]=delx*fabs(real(data,i))/sqrt(2*M_PI);
	}
	for (i = n/2+1; i < n; i++)
	{
	    fk[i-n/2-1]=delx*fabs(real(data,i))/sqrt(2*M_PI);
	}
	
	for (i = 0; i < n; i++)
	{
		fprintf (out, "%f  %f\n",k[i], fk[i]);
	}

	return 0;
}

