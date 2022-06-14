#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
int main() 
{
    char a = 'A';
    char *ptr = &a;
    printf("1 : %c || %c || %llu\n",a,*ptr,(uint64_t)ptr);
    
    char b = 'B';
    ptr = &b;
    printf("2 : %c || %c || %llu ",b,*ptr,(uint64_t)ptr);
    
    char c = 'C';
    ptr = &c;
    printf("\n3 : %c || %c || %llu ",c,*ptr,(uint64_t)ptr);

    (*ptr)++;
    printf("\n4 : %c || %c || %llu ",c,*ptr,(uint64_t)ptr);

    (*ptr)--;
    printf("\n5 : %c || %c || %llu ",c,*ptr,(uint64_t)ptr);

    unsigned x = 'S';
    ptr = (char *)&x;
    printf("\n6 : %c || %c || %llu ",x,*ptr,(uint64_t)ptr);
    printf("\n7 : %u || %c || %llu ",x,*ptr,(uint64_t)&x);


    int y = 34;
    y++;
    ptr = (char *)&y;
    printf("\n8 : %d || %d || %llu ",y,*ptr,(uint64_t)ptr);
    
    x = 0xABCD1234;
    ptr = (char *)&x;
    printf("\n9 : %x || %x || %c ",x,*ptr,*ptr);

    *ptr = 'C';
    printf("\n10 : %x || %x || %c ",x,*ptr,*ptr);

    unsigned *uint_ptr = (unsigned *)ptr;
    *uint_ptr = 'C';
    printf("\n11 : %u || %x || %x || %c \n",x,x,*ptr,*ptr);

    int *ptr1 = NULL;
    if (ptr1)
    {
      printf("12 | %d \n",*ptr1);
    }

    int someValue = 'K';
    if (!ptr1)
    {
        ptr1 = &someValue;
    }

    if (ptr1)
    {
        printf("13 | Pointer'S value : %c\n",*ptr1);
    }
    
    printf("\nEnd of Code\n");
    system("pause");

    return 0;
}