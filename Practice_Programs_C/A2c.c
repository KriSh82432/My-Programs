//Program 3
//To check whether the given number is positive or negative
#include <stdio.h>
#include <stdlib.h>
int main()
    {
        double number;
        printf("Enter the Number:");
        scanf("%lf",&number);

        if(number==0)
        {
            printf("The given Number is neither positive nor negative");
        }
        else
        {
            if(number>0){
                printf("The given Number is positive");
            }
            else{
                printf("The given Number is negative");
            }
        }
        return 0;
    }