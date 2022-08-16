from ast import Num


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


def squareRoot(num):
    return num**0.5


def modulus(num1, num2):
    return num1 % num2


def error1():
    print('Invalid Operator')
    main()


def areaOfCircle(pi, x):
    return pi*x*x


def methodFind():
    method = input("1. Num1/Num2 or 2.Num2/Num1 ? ")
    return method


def findFactorial(num):
    if num == 1:
        return 1
    else:
        return num * findFactorial(num-1)

def main():
    print("Select the operation from below: \n"
          "1.Addition\n"
          "2.Subtraction \n"
          "3.Multiplication\n"
          "4.Division \n"
          "5.Modulus\n"
          "6.Square root\n"
          "7.Area of circle\n"
          "8.Factorial\n")
    operator = input(
        'Select the matching number for the operation(1,2,3,4,5,6,7,8): ')
    cal(operator)
    


def cal(selectOperation):
    match selectOperation:
        case '1':
            print('You have selected Addition')
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(x, "+", y, "=", add(x, y))
        case '2':
            print('You have selected Subtraction')
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            sub = input(
                "Which operation yu want to do ? \n (1.Num1 - Num2 2.Num2 - Num1) : ")
            if sub == '1':
                print(x, "-", y, "=", subtract(x, y))
            elif sub == '2':
                print(y, "-", x, "=", subtract(y, x))
            else:
                print('Invalid input')
                pause()
        case '3':
            print('You have selected Multiplication')
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(x, "*", y, "=", multiply(x, y))
        case '4':
            print('You have selected Division')
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            try:
                method = methodFind()
                if method == '1':
                    ans = divide(x, y)
                    print(x, "/", y, "=", ans)
                elif method == '2':
                    ans = divide(y, x)
                    print(y, "/", x, "=", ans)
                else:
                    print("Invalid Input")
                    methodFind()
            except ZeroDivisionError as e:
                print("You cannot divide a number by 0"+" "+"(" + str(e)+")")
            except Exception as e:
                print("Something went wrong"+" "+"(" + str(e) + ")")
        case '5':
            print('You have selected Modulus')
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print(x, "%", y, "=", modulus(x, y))
        case '6':
            print('You have selected Square root')
            x = float(input("Enter the number: "))
            print("Square root of", x, "=", squareRoot(x))
        case '7':
            print('You have selected Area of Circle')
            pi = 3.14
            x = float(input("Enter the radius of the circle: "))
            print("Area of the circle with radius",
                  x, "=", areaOfCircle(pi, x))
        case '8':
            print("You have selected Factorial calculation\n")
            x = int(input("Enter the number: "))
            ans = findFactorial(x)
            print(str(x)+"! is equal to "+str(ans))
        case _:
            error1()
    pause()


while True:
    try:
        print('-----------------------------------------Welcome to the Simple Calculator-----------------------------------------(Coded by Krishna)')
        print("Press Ctrl+c to exit this program at any time...")
        main()
    except Exception as e:
        print("Something went wrong"+" "+"(" + str(e) + ")")
    except KeyboardInterrupt:
        print('\nThank you for using this program')
        exit()
