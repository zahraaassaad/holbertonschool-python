#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# number>0 is positive
# number<0 is negative
# number=0 is zero

if number > 0:
  print(number, 'is positive')
elif number == 0:
  print(number, 'is zero')
else:
  print(number, 'is negative')
