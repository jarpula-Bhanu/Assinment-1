//This code is to print the roots of the equation upto 3 significant digits

#include <stdio.h>
#include <math.h>

int main(){
    /*The quardratic equation is
        x^2-4x-8=0 int the form ax^2+bx+c=0
        roots are given by  "(-b+sqrt(b^2-4ac))/2a" and "(-b-sqrt(b^2-4ac))/2a"
    */
   int a=1,b=-4,c=-8;

   float root1 ,root2;

   root1=(-b+pow(b*b-4*a*c,0.5))/2*a;
   root2=(-b-pow(b*b-4*a*c,0.5))/2*a;

   printf("The roots of equation are\n");
   printf("%.2f and %.2f",root1,root2);

     
    return 0;
}