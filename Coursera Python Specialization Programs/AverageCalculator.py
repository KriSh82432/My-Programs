# Average Calculator 

def pause():
    programPause = input('Press any key to close...')   

num = 0.0
total = 0.0

while True:
   number = input('Enter a number: \n')
   if(number == 'Done'):
      break
   try:
      number1 = float(number)
   except:
      print('Invalid Input')
   num = num+1
   total = total+number1

print(total/num)

pause()