#include <stdio.h>

// a function which calculates y[i] takings array x and and i as parameters
float calculatey(int* p1,int  n){
	int y=0;
	if(n==0){y =*p1;}
	else if(n==1){y=*(p1+1)+calculatey(p1,0);}
	else if(n<6){y = *(p1+n-1) + *(p1+n-3) - calculatey(p1,n-1)/2.0;}
    else {y = -calculatey(p1,n-1)/2.0;}
	return y;
}


int main(){
	FILE* fp;
    int x[] = {1,2,3,4,2,1};
    float y[20];
    int i;
    for(int i=0;i<20;i++){
		y[i]=calculatey(x,i);}

	// opening file
    fp = fopen("y(n).dat","w");

	// writing to the file
    for(i=0;i<20;i++){
        fprintf(fp,"%f\n",y[i]);
    }
	// closing file
    fclose(fp);
    return 0; 
}