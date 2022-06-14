// Udemy C Bootcamp Pointers
// Application of constant pointers, constant to pointers

#include <stdio.h>
#include <stdlib.h>

int sum(int a, int b)
{
    int result = a + b;
    return result;
}

void printStudents(int totalStudents)
{
    printf("Total no. of students: %d",totalStudents);
}

int main()
{
    int boys,girls;
    printf("Enter the no. of boys and girls: \n");
    scanf("%d %d",&boys,&girls);
    int totalStudents = sum(boys,girls);
    printStudents(totalStudents);
    return 0;
    system("pause");
}
