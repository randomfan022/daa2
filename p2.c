#include<stdio.h> 
#include<stdlib.h> 
#include<math.h> 
#include<time.h> 
void bubble_sort(int a[],int n) 
{ 
 int i,j,temp; 
 for(i=0;i<n;i++) 
 { 
 for(j=0;j<n-i-1;j++) 
 { 
 if(a[j]>a[j+1]) 
 { 
 temp=a[j]; 
 a[j]=a[j+1]; 
 a[j+1]=temp; 
 } 
 } 
 } 
} 
int main(){ 
 int n,a[1000],i; 
 clock_t start,end; 
 double clk; 
 printf("ENTER THE NO. OF SEATS\n"); 
 scanf("%d",&n); 
 
 for(i=0;i<n;i++) 
 a[i]=rand()%1000; 
 
 printf("THE SEAT NO.S ARE:\n"); 
 for(i=0;i<n;i++) 
 printf("%d\t",a[i]); 
 printf("\n"); 
 
 start=clock(); 
 bubble_sort(a,n); 
 end=clock(); 
 clk=(double)(end-start)/CLOCKS_PER_SEC; 
 
 printf("THE SORTED SEAT NO.S ARE:\n"); 
 for(i=0;i<n;i++) 
 printf("%d\t",a[i]); 
 printf("\n"); 
 
 printf("TIME TAKEN FOR EXECUTION: %f\n",clk); 
}
