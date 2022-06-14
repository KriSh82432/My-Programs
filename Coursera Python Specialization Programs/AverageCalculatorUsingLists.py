# Average Calculator using lists 

def pause():
    pauseProgram = input("Press any key to close...")

numLists = list()

while True:
    inp = input('Enter a number: ')
    if inp == 'Done':
        break
    try:
     inp = float(inp)
     numLists.append(inp)
    except:
        print('Invalid Input')

average = sum(numLists) / len(numLists)
print("Average:", average)

pause()