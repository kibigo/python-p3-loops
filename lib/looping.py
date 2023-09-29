#!/usr/bin/env python3

def happy_new_year():
    counter = 11
    while counter > 1:
        counter -=1
        print(counter)
        if counter == 1:
            print("Happy New Year!")
        

def square_integers(int_list):
    squared_items = [integers ** 2 for integers in int_list]
    return (squared_items)


def fizzbuzz():

    for num in range(1, 101):
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        elif (num % 3 == 0):
            print("Fizz")
        elif(num % 5 == 0):
            print("Buzz")
        else:
            print(num)
    
