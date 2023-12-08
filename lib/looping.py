#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        if i == 1:
            print(i)
            print("Happy New Year!")
        else:             
            print(i)
        i -= 1    

def square_integers(int_list):
    sq_list = [num * num for num in int_list]
    return sq_list

def fizzbuzz():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: print(i)
        i += 1
