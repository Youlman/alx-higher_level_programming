#!/usr/bin/python3
import random
number = random.randint(-10, 10)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
print(f'Last digit of {number} is {last_digit} and is ', end="") 
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
elif last_digit < 6:
    print("less than 6 and not 0")
