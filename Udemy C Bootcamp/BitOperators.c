//Udemy C Bootcamp Practice Problem 4
//Use the bitmasks
#include <stdio.h>
#include <stdlib.h>
int main()
    {
     unsigned data=0xABCD;
     unsigned N=12,M=15;
     unsigned W=M-N+1;
     unsigned bitmasks=(1<<W)-1;
     unsigned result=(data>>N) & bitmasks;
     printf("data ----> %04X\n",data);
     printf("result ----> %04X\n",result);
     system("pause");
     return 0;

    }
