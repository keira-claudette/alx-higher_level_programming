#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    entry = "and is greater that 5"
elif last_digit == 0:
    entry = "and is 0"
elif (last_digit < 6) and (last_digit != 0):
    entry = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, entry))
