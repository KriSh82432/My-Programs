//Udemy C Bootcamp Practice Problem 7
//To calculate the minimum power of 2 greater than or equal to the user input
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int result,userInput;
     printf("Enter a positive number: ");
     scanf("%d",&userInput);  

    do
    {
      if(userInput>0)
      {
          result=1;
          while (result<userInput)
          {
               result*=2;
          }
          printf("Min. power of 2 greater than %d : %d\n",userInput,result);
          break;
      }
    } while (userInput != -1);
    return EXIT_SUCCESS;
}
