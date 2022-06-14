//Udemy C Bootcamp Practice Problem 10
//To find all the prime numbers below a upper limit

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

const int MAX = 1000;

bool isPrime( int number)
 {
    for (int i = 2; i < number; i++)
    {
        if (number % 2 == 0)
        {
            return false;
        }
        
    }
    return true;
 }

void printLimitError()
 {
    printf("Error: Must be 2<limit<MAX\n");
 }

bool isOutOfBounds(limit)
 {
    return (limit < 2 || limit > MAX);
 }

int main() 
 {
    int upperLimit;
    printf("Enter the upper limit: ");
    scanf("%d",&upperLimit);

    if(isOutOfBounds(upperLimit))
    {
        printLimitError();
        return EXIT_FAILURE;
    }

    for (int number = 2; number < upperLimit; number++)
    {
        if(isPrime(number))
        {
            printf("%d\n",number);
        }
    }
     system("pause");

    return EXIT_SUCCESS;

 }