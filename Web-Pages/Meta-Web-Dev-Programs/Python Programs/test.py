print('Hello', 'World', sep=': :')
print('Hello', 'World', sep=': :', end='\n')
print("I love {1} and {0}".format('Python', 'C++'), end='\n')
print("I love {1} and {0}".format('Python', 'C++'), end='\n')

height = float(input('What is your height in meters? '))    
print(f"Type of height variable is: {type(height)}. It should be <class 'float'>. Height is %.2f"%height)
loyalty = bool(input('Are you part of our loyalty program? '))
print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")


coffee = input('1 coffee @: $ ')
sandwich = input('1 sandwich @: $ ')
cake = input('1 cake @: $ ')
bill_total = float(coffee) + float(sandwich) + float(cake)
print('Your total bill is $ %.2f' % bill_total)


a = isinstance("aa", str)
print(a)

b = 3
print(not(b>5))
 
def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print('2',isPalindrome('racecar'))

str1 = 'reversal'
new_str = str1[::-1]
print(new_str)