# Recursion method to find factorial of a number
def findFactorial(number):
    if number == 1:
        return 1
    else:
        return number * findFactorial(number-1)

num = int(input("Enter a number: "))
print("Answer is ", findFactorial(num))

# Tower of Hanoi and disks problem
def hanoi(disks, source, helper, destination):
    if disks == 1:
        print('Disk {} moves from {} to {}.'.format(disks, source, destination))
        return
    hanoi(disks-1, source, destination, helper)
    print('Disk {} moves from {} to {}.'.format(disks, source, destination))
    hanoi(disks-1, helper, source, destination)

disks = int(input("Enter no. of disks: "))
print("Moves: ")
hanoi(disks, 'A', 'B', 'C')

# Reversing a string using recursion

def reverseString(word):
    if len(word) == 0:
        return word
    else:
        return reverseString(word[1:]) + word[0]

word = str(input("Enter a word: "))
rev_str = reverseString(word)
print("Reversed word is {}".format(rev_str))