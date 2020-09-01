#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#print number
#print its last digit
#print >5 or ==0 or <6 and !=0

number=str(number)

if number[0]>5:
  print('Last digit of {} is {} and is greater than 5'.format(number,number[-1:]))
elif number[-1:]==0:
  print('Last digit of {} is {} and is 0'.format(number,number[-1:]))
elif number[-1:]<6:
  print('Last digit of {} is {} and is 0'.format(number,number[-1:]))
