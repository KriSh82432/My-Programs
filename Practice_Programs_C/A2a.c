//Program 1
//To chech the given number is even or odd
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int number;
    printf("Enter the Number:");
    scanf("%d",&number);

    if(number%2==0)
    {
        printf("The Given Number is Even");
    }
    else{
        printf("The Given Number is Odd");
    }
    return 0;
}