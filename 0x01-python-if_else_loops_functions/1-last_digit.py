#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#print number
#print its last digit
#print >5 or ==0 or <6 and !=0

if int(str(number)[-1])>5:
  print('Last digit of {} is {} and is greater than 5'.format(number,str(number)[-1]))
elif int(str(number)[-1])==0:
  print('Last digit of {} is {} and is 0'.format(number,str(number)[-1]))
elif int(str(number)[-1])<6 and int(str(number)[-1])!=0:
  print('Last digit of {} is {} and is 0'.format(number,str(number)[-1]))
