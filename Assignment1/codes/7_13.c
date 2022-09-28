#include<stdio.h>
#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <complex.h>
complex W(int k ,int N){
    return cos((2*M_PI*k)/N) - I*sin((2*M_PI*k)/N) ;
}
complex fft(int k ,int a[],int n,int N){
    if(n == 1){
        return a[0] ;
    }
    int e[n/2] ;
    int o[n/2] ;
    for(int i = 0 ;i < n ;i++){
        if(i%2 == 0){
            e[i/2] = a[i] ;
        }
        else{
            o[(i-1)/2] = a[i] ;
        }
    }
    return fft(k,e,n/2,N)+W(k,n)*fft(k,o,n/2,N) ;
}

int main(){
    int n = 8;
	int a[8] = {1,2,3,4,2,1,0,0} ;
    for(int i = 0 ;i < 8 ; i++){
    printf("%lf %lf\n",creal(fft(i,a,8,8)),cimag(fft(i,a,8,8))) ;
    }

}