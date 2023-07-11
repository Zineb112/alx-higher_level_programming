#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = repr(number)
last_str = str_num[-1]
last_digit = int(last_str)

if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is 0 and is 0".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_digit))
