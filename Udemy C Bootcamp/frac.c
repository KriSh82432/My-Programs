#include <stdio.h>
#include <stdlib.h>

int main()
{
    float num;
    scanf("%f",&num);
    int num1;
    num1 = (int)num;
    float fracPart;
    fracPart = num - num1;
    printf("IntegeDDr Part: %d\n",num1);
    printf("Fractional Part: %.3f",fracPart);

    return 0;
}