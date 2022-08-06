def pause():
    pauseProgram = input(
        "Press 'C' to continue calculating or 'Q' to quit... ")
    if pauseProgram == 'C' or pauseProgram == 'c':
        main()
    elif pauseProgram == 'Q' or pauseProgram == 'q':
        print('Thank you for using this program')
        exit()
    else:
        print('Invalid input')
        pause()


selectOperation = None


def add(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


def divide1(num1, num2):
    return num2/num1


def error():
    print('Invalid input for division (Denominator cannot be 0)')
    pause()


def squareRoot(num):
    return num**0.5


def modulus(num1, num2):
    return num1 % num2


def error1():
    print('Invalid Operator')


def areaOfCircle(pi, x):
    return pi*x*x


def main():
    print('-----------------------------------------Welcome to the Simple Calculator-----------------------------------------(Coded by Krishna)')
    print("Select the operation from below: \n"
          "1.Addition\n"
          "2.Subtraction \n"
          "3.Multiplication\n"
          "4.Division \n"
          "5.Modulus\n"
          "6.Square root\n"
          "7.Area of circle\n")
    operator = int(
        input('Select the matching number for the operation(1,2,3,4,5,6,7): '))
    cal(operator)


def cal(selectOperation):
    if selectOperation == 1:
        print('You have selected Addition')
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(x, "+", y, "=", add(x, y))

    elif selectOperation == 2:
        print('You have selected Subtraction')
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        sub = input("Which operation yu want to do ? \n (1.Num1 - Num2 2.Num2 - Num1) : ")
        if sub == '1':
            print(x, "-", y, "=", subtract(x, y))
        elif sub == '2':
            print(y, "-", x, "=", subtract(y, x))

    elif selectOperation == 3:
        print('You have selected Multiplication')
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        print(x, "*", y, "=", multiply(x, y))

    elif selectOperation == 4:
        print('You have selected Division')
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        if (y == 0):
            error()
        elif (x >= y):
            print(x, "/", y, "=", divide(x, y))
        elif (y > x):
            print(y, "/", x, "=", divide1(x, y))

    elif selectOperation == 5:
        print('You have selected Modulus')
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        if(y != 0):
            print(x, "%", y, "=", modulus(x, y))
        else:
            error()

    elif selectOperation == 6:
        print('You have selected Square root')
        x = float(input('Enter the number: '))
        squareRootNumber = float(input('Enter the numnber: '))
        print(x, "^", "=", squareRoot(x))

    elif selectOperation == 7:
        print('You have selected Area of Circle')
        x = float(input('Enter the radius: '))
        pi = 3.148
        print('Area of the circle', "=", areaOfCircle(pi, x), "sq.unitskk")

    elif selectOperation is None:
        pass

    else:
        error1()


while True:
    try:
        main()
        pause()
    except KeyboardInterrupt:
        print('Thank you for using this program')
        exit()