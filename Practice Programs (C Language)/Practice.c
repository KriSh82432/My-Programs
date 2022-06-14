#include <stdio.h>
#include <stdlib.h>

int main() 
{
    int T;
    printf("Enter the no. of test cases: \n");
    scanf("%d",&T);

    while (T--)
    {
        char operator;
        printf("Enter the operator: \n");
        scanf("%c",&operator);
       
        int a,b;
        printf("Enter the two numbers: \n");
        scanf("%d %d",&a,&b);

        switch (operator)
        {
        case ('+'):
            printf("%d + %d = %d\n",a,b,(a+b));
            break;
        case ('-'):
             printf("%d - %d = %d\n",a,b,(a-b));
             break;
        case ('*'):
            printf("%d * %d = %d\n",a,b,(a*b));
            break;
        case ('/'):
            if (a>b)
            {
                printf("%d / %d = %d\n",a,b,(a/b));
            }
            else{
                printf("Unable to divide. The divisor is greater than the dividend");
            }
            break;
        default:
            printf("Invalid operator\n");
            break;
        }   
    }
    
    return 0;
}