#include <stdio.h>  
#include <stdlib.h>  
   
int main()  
{   char ch;  
    FILE *file;  
    int count = 0;  
      
    //Opens a file in read mode  
    file = fopen("words.txt","r");  
      
    //Gets each character till end of file is reached  
    while((ch = fgetc(file)) != EOF){  
        //Counts each word  
        if(ch ==' ' || ch == '\n')  
            count++;  
    }  
      
    printf("Number of words present in given file: %d", count);  
    fclose(file);  
      
    return 0;  
}  