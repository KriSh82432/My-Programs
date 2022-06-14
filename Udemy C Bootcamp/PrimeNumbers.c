//Udemy C Bootcamp Practice Problem 9
//Find all the prime numbers above a upper limit (user input)
//Find the first prime number greater than the lowert limit (user input)

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main()
{
    const int max=1000;
    int upperLimit;
    printf("Enter the Upper Limit: ");
    scanf("%d",&upperLimit);

    if(upperLimit<2 || upperLimit>max)
    {
        printf("Invalid Input...Must be 2<upperLimit<max\n");
        goto exit_program;
    }

      printf("Prime Numbers from %d: \n",upperLimit);
      for (int number = 2; number < upperLimit; number++)
      {
          bool isPrime = true;
          for (int i = 2; i < number; i++)
          {
              if(number%2==0)
              {
                  isPrime=false;
                  break;
              }
          }
          if(isPrime)
          {
              printf("%d\n",number);
          }
          
      }
      
      int lowerLimit;
      printf("Enter the lower limit: ");
      scanf("%d",&lowerLimit);

      if(lowerLimit<2 || lowerLimit>max)
    {
        printf("Invalid Input...Must be 2<upperLimit<max\n");
        goto exit_program;
    }
      int firstPrime=-1;

     for (int number = lowerLimit; number < max; number++)
     {
         bool isPrime = true;
          for (int i = 2; i < number; i++)
          {
              if(number%i==0)
              {
                  isPrime=false;
                  break;
              }
          }
          if(isPrime)
          {
              firstPrime=number;
              break;
          }
     }
     
     if(firstPrime==-1)
     {
         printf("Unable to find a prime number above %d",firstPrime);
     }        
     else
     {
         printf("The first prime number above %d : %d",lowerLimit,firstPrime);
     }
        exit_program:
        printf(".................................\n");
        printf("......Some dummy cleanup code....");
     system("pause");

        return EXIT_SUCCESS;
}