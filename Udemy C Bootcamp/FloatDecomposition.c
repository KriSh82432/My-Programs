// Udemy C Bootcamp - Pointers Problem 15
// Take a floating point number and print the integer part and fractional part of the input 

#include <stdio.h>
#include <stdlib.h>

void decompose(float number, int *int_part, float *frac_part)
{
    *int_part = (int)number;
    *frac_part = number-*int_part;
}

int main()
{
    int int_part;
    float frac_part,input;
    printf("Enter a floating point number: \n");
    scanf("%f",&input);

    decompose(input,&int_part,&frac_part);
    
    printf("Integer part of %.3f : %d\n",input,int_part);
    printf("Fractional part of %.3f : %.3f\n",input,frac_part);
    
    float num;
    printf("Reconstructed Number: %.3f\n",(int_part+frac_part));
    return 0;
}