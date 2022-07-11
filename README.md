#### Day 2 Project

## Python primitive data types

Strings, Int, Float, Boolean. 

"Hello" is a string with five characters together.

print("Hello"[0]) --> will return H 

Method of pulling out a specific elemnent of a string is called "Subscript"

If you want to separate a number for example 123456789 like 123,456,789 to make it more readable, you might need to use underscore (_) instead of commas (,) to avoid issues.

## Type Error, Type Checking, Type Conversion

Type Error example:

stdin: len(4837)
stdout: TypeError: object of type 'int' has no len()

stdin: print("Your name has " + 5 + " characters.")
stdout: TypeError: can only concatenate str (not "int") to str

type() --> gives the type of data 

print(type(5)) - Output: class 'Integer'

str() --> converts to string

## Mathematical Operations in Python

3 + 5
7 - 4
3 * 2
6 / 3 -- > Note: when you divide a number you'll always end with a float number.

2 ** 2 --> exponent

PEMDAS (Left to Right) - (Order of priorities in operations)
Parentheses
Exponent
Multiplication - Division
Addition - Substraction

print(3 * 3 + 3 / 3 - 3) - Output: ( 9 + 1 - 3) --> 7

## Number Manipulation and F Strings in Python

round() --> to round numbers
round(number,3) --> round to 3 decimals


8 // 3 --> automatically converts division into a integer

number += 1 --> number = number + 1
number /= 2 --> number = number / 2
etc etc...

F-Strings: Use curly braces and F strings to easily insert different data types into a string

example:

print ("Your score is " + str(score)) ----> drake meme picture 1 >:(

print (f"Your score is {score}) ----> drake meme picture 2 >:)

## Additional Notes from exercise (main.py)

Do not try to save a variable with a print statement if you intend to do a mathematical operation (e.g: totalBill = print(input("What was the total bill"))) since this datatype is NoneType. 