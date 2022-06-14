//Program 2
//To check the first number is greater than or lesser than the second number
#include <stdio.h>
#include <stdlib.h>
int main()
{
    double num1,num2;
    printf("Enter the two numbers:");
    scanf("%lf %lf",&num1,&num2);
     
     if(num1==num2){
        printf("The given two numbers are equal");
     }
     else{
        if(num1>num2){
        printf("The first number(%lf) is greater than the second number(%lf)",num1,num2);
    }
    else{
        printf("The first number(%lf) is lesser than the second number(%lf)",num1,num2);
    }
     }
    return 0;
}