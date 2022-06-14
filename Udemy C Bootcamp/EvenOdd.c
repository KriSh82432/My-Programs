//Udemy C Bootcamp Practice Problem 5
//To check a positive number whether it is odd or even
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main()
    {
        int number;
        printf("Enter a positive number: ");
        scanf("%d",&number);
        
        //Check the numbe whether it is positive or negative
        if(number<0)
        {
         printf("Invalid Input(%d)",number);
         return EXIT_FAILURE;   
        }
        bool isEven=(number%2==0)? true : false ;
        if(isEven)
        {
            printf("The entered number is Even");
        }
        else
        {
          printf("The enetered number is Odd");
        }

     system("pause");
    
        return EXIT_SUCCESS;
    }