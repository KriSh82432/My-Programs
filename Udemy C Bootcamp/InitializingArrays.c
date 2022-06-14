// Iniatilizing arrays

#include <stdio.h>
#include <stdlib.h>

#define len 5 // We cannot use variables or constants in the place of index in list arrays
int main()
{
    int array[len];

    for (int i = 0; i < len; i++)
    {
        int value;
        printf("Enter a value: ");
        scanf("%d", &value);
        array[i] = value;
    }

    // Initialization of arrays using brace - enclosed lists
    int x[] = {2, 4, 5}; // x has type int and holds 2, 4, 5
    int y[len] = {1, 2, 3}; // y has type int and holds 1, 2, 3, 0, 0
    int z[len] = {2, 3, 4, 5}; // z has type int and holds 2, 3, 4, 5, 0

    // Initialization of Arrays with designators (Sparse Arrays)

    int b[len] = {[1] = 2, [2] = 3}; // b has type int and holds 0, 2, 3, 0, 0
    int c[len] = {[0] = 3, [len-1] = 3}; // c has type int and holds 3, 0, 0, 0, 3
    
    printf("%d",z[len]);
    return 0;
}