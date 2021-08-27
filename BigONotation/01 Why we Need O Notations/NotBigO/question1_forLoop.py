'''
    Write a program to calculete sum of n natural numbers.
    For example, we will take n as 100

    -> Using For Loop
    -> Using While Loop
'''
import time
time.time()

timestamp1 = time.time()

###python Program to find Sum of N natural Numbers ###
number = 100
total = 0

for value in range(1, number + 1):
    total = total + value
print("The sum is", total)

### Program Completed ###

timestamp2 = time.time()
print((timestamp2 - timestamp1))