//Udemy C Bootcamp Practice Problem 6
//To print the day using a numeric input
#include <stdio.h>
#include <stdlib.h>

typedef enum
{
    Monday=1,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
} DayOfWeek;
 
int main() 
{
 printf("-------Days of the Week-------\n");
 printf("Monday/Sunday : %d/%d\n", Monday, Sunday);
 
 DayOfWeek day;
 printf("Enter the input (1 to 7) : \n");
 scanf("%d",&day);

 switch (day)
 {
 case Monday:
     printf("%d is Monday\n",day);
     break;
 case Tuesday:
     printf("%d is Tuesday\n",day);
     break;
 case Wednesday:
     printf("%d is Wednesday\n",day);
     break;
 case Thursday:
     printf("%d is Thursday\n",day);
     break;
 case Friday:
     printf("%d is Friday\n",day);
     break;
 case Saturday:
     printf("%d is Saturday\n",day);
     break;
 case Sunday:
     printf("%d is Sunday\n",day);
     break;                     
 default:
     printf("Invalid Input. Enter a number between this range[1,7]");
     break;
 }
     system("pause");

return EXIT_SUCCESS;

}
