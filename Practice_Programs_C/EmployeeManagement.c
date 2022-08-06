#include <stdio.h>
#include <stdlib.h>
#include <string.h>

 
struct emp
{
  
char name[50];
   
float salary;
   
int age;
   
int id;
 
};

struct emp e[100];

 
long int size = sizeof (e);

 
int i = 0, count = 0;

 
 
FILE * fp;

 
void addrecord () 
{
  
 
fp = fopen ("data.txt", "w");
  
printf ("\nEnter name = ");
  
scanf ("%s", e[i].name);
  
 
printf ("\nEnter Age = ");
  
scanf ("%d", &e[i].age);
  
 
printf ("\nEnter Salary = ");
  
scanf ("%f", &e[i].salary);
  
printf ("\nEnter EMP-ID : ");
  
scanf ("%d", &e[i].id);
  
fwrite (&e[i], size, 1, fp);
  
if (fp == NULL)
    
    {
      

	printf ("\nCannot open file...");
      
exit (EXIT_FAILURE);
    
}
  
 
 
 
 
 
   
    printf ("\n\nFile created and saved successfully. :) \n\n\n");

 
 
 
}


 
 
 

  void displayrecord () 
{
  
 
 rewind(fp);
 fp = fopen("data.txt", "r");

for (i = 0; i < count; i++)
    
    {
      while (fread (&e[i], size, 1, fp))
	{
	  
printf ("\n Employee name = %s", e[i].name);
	  
 
printf ("\n\t Age = %d", e[i].age);
	  
 
printf ("\n\t  Salary = %f", e[i].salary);
	  
printf ("\n\t  ID = %d", e[i].id);
	
}
    
 
}

 
}



  int main () 
{
  
int choice;
  
 
  
 
 
 
 
printf ("\n\t\t\t\t[|:::>:::>:::>::> " 
		       "EMPLOYEE RECORD <::<:::<:::" 
 "<:::|]\t");
  
 
 
 
 
while (1)
    {
      

	
 
printf ("\n1. ADD RECORD\n");
      
 
 
 
printf ("\n3. DISPLAY RECORDS\n");
      
 
 
 
printf ("\n5. EXIT\n");
      
 
printf ("\nENTER YOUR CHOICE...\n");
      
fflush (stdin);
      
scanf ("%d", &choice);
      
 

	switch (choice)
	{
	
case 1:
	  
	    addrecord ();
	  
i++;
	  
count++;
	  
fclose (fp);
	  
break;
	
 
 
case 2:
	  
 
	   
	    displayrecord ();
	  

	  
break;
	
 
 
 
case 3:
	  
fclose (fp);
	  
exit (0);
	  
break;
	
 
default:
	  
printf ("\nINVALID CHOICE...\n");
	
}
    
}
  
 
return 0;

}