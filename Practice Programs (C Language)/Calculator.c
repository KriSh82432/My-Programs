//Simple calculator in C which takes 4 operators +,-,*,/
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char operator;
    printf("Enter the Operator :( +, -, *, /)");
    scanf("%c", &operator);

    double first, second;
    printf("Enter the two numbers separated by a space : ");
    scanf("%lf %lf", &first, &second);

    switch (operator)
    {
    case ('+'):
        printf("%lf + %lf = %lf", first, second, (first + second));
        break;

    case ('-'):
        printf("%lf - %lf = %lf", first, second, (first - second));
        break;

    case ('*'):
        printf("%lf * %lf = %lf", first, second, (first * second));
        break;

    case ('/'):
        if (second != 0.0)
        {
            printf("%lf / %lf = %lf", first, second, (first / second));
        }
        else
        {
            printf("Invalid input");
        }
        break;

    default:
        printf("Invalid operator");
    }
    system("pause");
    return 0;
}