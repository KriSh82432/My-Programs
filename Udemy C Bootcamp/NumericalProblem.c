//Udemy C Bootcamp Practice Problem 1
#include <stdio.h>
#include <stdlib.h>

int main()
{
    const int moonLanding=1969;
    const double LightYear=299792458;
    const float pi=3.142;
    const unsigned hexaDead=0xDEAD;
    const unsigned hexaSecret=5196;
    printf("moonLanding: \n %10d\n %010d\n",moonLanding,moonLanding);
    printf("LightYear: \n %9f\n %.3e\n",LightYear,LightYear);
    printf("pi: \n %.2f\n %.1e\n",pi,pi);
    printf("hexaDead: \n 0x%X\n %.6x\n",hexaDead,hexaDead);
    printf("hexaSecret: \n %x",hexaSecret);
     system("pause");

    return 0;
}