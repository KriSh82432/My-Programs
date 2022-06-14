//Udemy C Bootcamp Practice Problem 3 
//Calculating area and volume of sphere
#include <stdio.h>
#include <math.h>
int main()
{
    double radius;
    printf("Enter the radius of the Sphere: ");
    scanf("%lf",&radius);
    double AreaOfSphere,VolumeOfSphere;
    const double pi=3.14159265359;
    AreaOfSphere=4*pi*radius*radius;
    VolumeOfSphere=(4/3)*pi*radius*radius*radius;
    printf("Area of the Sphere: %.2lf\n                    %.3e\n",AreaOfSphere,AreaOfSphere);
    printf("Volume of the Sphere: %.2lf\n                      %.3e",VolumeOfSphere,VolumeOfSphere);
     system("pause");

    return 0;
}