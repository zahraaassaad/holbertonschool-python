#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# number>0 is positive
# number<0 is negative
# number=0 is zero

if number > 0:
  print(number, "is positive")
    print('{} is positive'.format(number))
elif number == 0:
  print(number, "is zero")
    print('{} is zero'.format(number))
else:
  print(number, "is negative")
    print('{} is negative'.format(number))
