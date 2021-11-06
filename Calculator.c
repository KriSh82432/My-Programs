#include <stdio.h>
int main()
{
    char operator;
    printf("Enter the Operator :( +, -, *, /)");
    scanf("%c",&operator);

    double first,second;
    printf("Enter the two numbers separated by a space : ");
    scanf("%lf%lf",&first,&second);
     
    switch (operator){
    case('+'):
       printf("%lf + %lf = %lf",first,second,(first+second));
        break;
    
    case ('-'):
       printf("%lf - %lf = %lf",first,second,(first-second));
        break;

    case ('*'):
       printf("%lf * %lf = %lf",first,second,(first*second));
        break;

    case ('/'):
       if (second != 0.0){
           printf("%lf / %lf = %lf",first,second,(first/second));
       }
       else {
           printf("Invalid input");
       }
    break;
    
    default:
       printf("Invalid operator");
    
    }
    return 0;
}