//Udemy C Bootcamp Practice Problem 8
//To draw sigma symbol using for loop

#include <stdio.h>
#include <stdlib.h>

int main()
{
    const char symbol ='x';
     int BASE_WIDTH;
     printf("Enter the base width: ");
     scanf("%d",&BASE_WIDTH);

    int TIP_WIDTH;
    printf("Enter the tip width: ");
    scanf("%d",&TIP_WIDTH);
    int i,j;

    for ( i = 0; i < BASE_WIDTH; i++)
    {
        printf("%c",symbol);
    }
    printf("\n");

    for ( i = 1; i < TIP_WIDTH; i++)
    {
        for ( j = 0; i > j; j++)
        {
            printf(" ");
        }
        printf("%c\n",symbol);
     }
     
     for ( i = TIP_WIDTH; i > 1; i--)
     {
        for ( j = 0; i > j; j++)
        {
         printf(" ");
        }
     printf("%c\n",symbol);
     }
    for ( i = 0; i < BASE_WIDTH; i++)
    {
        printf("%c",symbol);
    }
    printf("\n");
     system("pause");

    return 0;
}