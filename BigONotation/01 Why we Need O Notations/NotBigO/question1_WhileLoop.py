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
num = 100

if num < 0:
    print("Enter a positive Number")
else:
    sum = 0
    # Use While loop to iterate until zero
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)


### Program Completed ###

timestamp2 = time.time()
print((timestamp2 - timestamp1))