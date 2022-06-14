// Udemy C Bootcamp - Arrays Introduction
// Why should we use arrays??
// The answer is the program that follows

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int io_count = 0;
    int max_count;
    printf("Enter the numbe of rows: ");
    scanf("%d", &max_count);
    float io_array[max_count];

    printf("Enter the amount: \n");
    for (io_count >= 0; io_count < max_count; io_count++)
    {
        float value;
        printf("%d|%d: ", io_count, max_count);
        scanf("%f", &value);

        if (value == 0)
        {
            break;
        }

        io_array[io_count] = value;
    }

    printf("..............\n");

    float sum = 0;
    for (int i = 0; i < io_count; i++)
    {
        sum += io_array[i];
        printf("%d | %.2f $\n", i, io_array[i]);
    }

    printf("..............\n");
    printf("Sum | %.2f $\n", sum);
    return EXIT_SUCCESS;
}