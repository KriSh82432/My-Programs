#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <windows.h>
#define DAT 10000


struct library
{
char bk_name[30];
char publisher[30];
int  price;
};

int main()
{
FILE *ptr,*view;
struct library l[100];
char pb_nm[30],bk_nm[30];
int i,j, keepcount;
i=j=keepcount = 0;


printf("\n\n########################## Library Management ##########################\n");
while(j!=5)
{
printf("\n1. Add book information\n");
printf("2. Display All Books Available \n");
printf("3. Display Highest Price Book\n");
printf("4. Display list of Publishers\n");
printf("5. Exit");
printf("\n\n########################## by GOWSHIK RAM R ##########################\n");
printf ("\n\nEnter one of the above : ");
scanf("%d",&j);

switch (j)
{
/* Add book */
case 1:

ptr=fopen("record.txt","w");
	printf ("Enter book name = ");
	scanf ("%s",l[i].bk_name);
	printf ("Enter publisher name = ");
	scanf ("%s",l[i].publisher);
	printf ("Enter price = ");
	scanf ("%d",&l[i].price);
	fflush(stdin);
	fprintf(ptr,"%s %s %d",l[i].bk_name,l[i].publisher,l[i].price);	
keepcount++;
fclose(ptr);
break;

case 2:

	printf("Display All Books Available\n");
view=fopen("record.txt","r");

while(fscanf(ptr,"%s %s %d",l[i].bk_name,l[i].publisher,&l[i].price)!=EOF){
	printf("\n book name =%s \t author name = %s  \t  price = %d",l[i].bk_name,l[i].publisher,l[i].price);
}
fflush(stdin);
fclose(view);
	break;

case 3:
	printf ("Highest Price Book : ");
float temp = 0;
	for (i=0;i<keepcount;i++)
	{
	    if(temp < l[i].price)
	        temp = l[i].price;
	}
	printf("%f", temp);
	
	break;

case 4:
	printf ("List of Publishers : ");
	for (i=0;i<keepcount;i++)
	{
	    printf ("\n %s ",l[i].publisher);
	}
	break;

case 5:
	exit (0); 
}
}
printf("\n\n########################## BY GOWSHIK RAM R  ##########################\n");
return 0;
}