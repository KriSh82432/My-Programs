//Udemy C Bootcamp Practice Problem 2
#include <stdio.h>
#include <stdlib.h>

typedef enum {
    NONE=0,
    LOW=5,
    MEDIUM=9,
    HIGH=12,
    MAXIMUM=20,
}ThrustLevel;

int main()
    {
        ThrustLevel Thrust;
        Thrust=NONE;
        printf("Rocket Thrust Level: %d\nRocket is ready to go....\n",Thrust);

        Thrust= MAXIMUM;
        printf("Rocket Thrust Level: %d\nRocket is ready to take off....\n",Thrust);

        Thrust=MEDIUM;
        printf("Rocket Thrust Level: %d\nRocket is entering into the Ionosphere....\n",Thrust);

        Thrust=LOW;
        printf("Rocket Thrust Level: %d\nRocket is traveling in space...\n",Thrust);
     system("pause");

return 0;
    }