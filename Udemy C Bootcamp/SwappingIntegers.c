// Udemy C Bootcamp - Pointers Problem 14
// Swapping Integers using pointers

#include <stdio.h>
#include <stdlib.h>

void swap(int *const p1, int *const p2)
{
    int temp;
    temp = *p2;
    *p2  = *p1;
    *p1 = temp;
}
int main()
{
    int apples,pears;
    printf("Enter the no. of Apples and Pears :  ");
    scanf("%d %d",&apples,&pears);
    printf("Before Swapping: Apples=%d, Pears=%d\n",apples,pears);

    int *pApples = &apples;
    int *pPears = &pears;
    swap(pApples,pPears);
    
    printf("After Swapping: Apples=%d, Pears=%d\n",apples,pears);

    swap(&apples,&pears);
    printf("After Second Swapping: Apples=%d, Pears=%d\n",apples,pears);

    return 0;
}