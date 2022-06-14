//Udemy C Bootcamp Practice Problem 11
//A simple problem to practice debugging
#include <stdio.h>
#include <stdlib.h>

int cumulativeSum(int limit)
{
    int result = 0;
    for (int i = 1; i <= limit; i++)
    {
        result += i;
    }
    return result;
}

int main() 
{
    int number = 15;
    int factor = 3;

    printf("Number before multiplication: %d\n",number);

    number *= factor;
    printf("Number after multiplication: %d\n",number);
    
    int sum = cumulativeSum(number);
    printf("Cumulative Sum upto %d : %d\n",number,sum);
     system("pause");

    return 0;

}

