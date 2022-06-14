#include <stdio.h>
#include <stdlib.h>
union Time
{
    int hours,minutes,seconds;
};
int main()
{
    union Time startTime,stopTime,diff;
    scanf("%d %d",&startTime.hours,&stopTime.hours);
    diff.hours=(startTime.hours-stopTime.hours);
    scanf("%d %d",&startTime.minutes,&stopTime.minutes);
    diff.minutes=(startTime.minutes-stopTime.minutes);
    scanf("%d %d",&startTime.seconds,&stopTime.seconds);
    diff.seconds=(startTime.seconds-stopTime.seconds);
    printf("%d\n%d\n%d\n",diff.hours,diff.minutes,diff.seconds);
    return 0;
}