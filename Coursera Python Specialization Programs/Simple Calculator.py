def pause():
    pauseProgram = input('Press any key to continue')

def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def subtract1(num1,num2):
    return num2-num1
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def divide1(num1,num2):
    return num2/num1
def error():
    print('Invalid input')
def squareRoot(num):
    return num**0.5
def modulus(num1,num2):
    return num1%num2
def error1():
    print('Invalid Operator')
def areaOfCircle(pi,x):
    return pi*x*x

print("Select the operation from below: \n"
            "1.Addition\n" 
            "2.Subtraction \n"
            "3.Multiplication\n" 
            "4.Division \n"
            "5.Modulus\n"
            "6.Square root\n"
            "7.Area of circle\n" )
selectOperation = int(input('Select the matching number for the operation(1,2,3,4,5,6,7): '))

x = 0
y = 0

if selectOperation == 1:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x ,"+", y, "=", add(x,y))

elif selectOperation == 2:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if (x>y) :
      print(x ,"-", y, "=", subtract(x,y))
    elif (y>x) :
      print(y ,"-", x, "=", subtract1(x,y))

elif selectOperation==3:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if (x!=0 and y!=0):
     print(x ,"*", y, "=", multiply(x,y))
    elif (x==0 or y==0):
        error()

elif selectOperation==4:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: ")) 
    if (y==0):
        error()
    elif (x>=y):
      print(x ,"/", y, "=", divide(x,y))
    elif (y>x):
      print(y ,"/", x, "=", divide1(x,y))
 
elif selectOperation==5:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x ,"%", y, "=", modulus(x,y))

elif selectOperation==6:
    x = float(input('Enter the number: '))
    squareRootNumber = int(input('Enter the numnber: ')) 
    print(x ,"^", "=", squareRoot(x,y))

elif selectOperation==7:
    x = float(input('Enter the radius: '))
    pi = 3.148
    print('Area of the circle',"=" ,areaOfCircle(pi,x) , "sq.unitskk") 

else :
    error1()


pause()
exit()