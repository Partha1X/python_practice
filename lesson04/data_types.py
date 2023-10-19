import math  # Import the math module

# String data Type

# Literal assignment
first = "Partha"  # Assign the string "Partha" to the variable 'first'
last = "Biswas"  # Assign the string "Biswas" to the variable 'last'

# Concatenation
fullname = first + " " + last  # Concatenate 'first' and 'last' with a space in between
print(fullname)  # Print the full name
fullname += "!"  # Add an exclamation mark to the 'fullname' string
print(fullname)  # Print the updated 'fullname'

# Casting a Number to a String
decade = str(1980)  # Convert the integer 1980 to a string
print(type(decade))  # Print the data type of 'decade' (should be str)
print(decade)  # Print the 'decade' string

statement = "I like Bengali, Hindi & English Song from The " + decade + "s."  # Create a statement with the 'decade' string
print(statement)  # Print the statement

# Multiple Lines
multiline = '''
Hey How Are You 

I was just Checking in .
                            All Good ?

'''
print(multiline)  # Print the multiline text

# Escaping Special Characters
sentence = 'I\'m back at work !\tHey!\n\nWhere\'s this at \\located ?'  # Use escape characters for special characters
print(sentence)  # Print the 'sentence'

# String Methods

print(first)  # Print the 'first' string
print(first.lower())  # Print 'first' in lowercase
print(first.upper())  # Print 'first' in uppercase

print(multiline.title())  # Print 'multiline' with title case
multiline = multiline.replace("Good", "Ok")  # Replace "Good" with "Ok" in 'multiline'
print(multiline)  # Print the updated 'multiline'

print(len(multiline))  # Print the length of 'multiline'
multiline += "                                   "  # Add spaces to 'multiline'
multiline = "                                    " + multiline  # Add more spaces to 'multiline'
print(len(multiline))  # Print the updated length of 'multiline'

print(len(multiline.strip()))  # Print the length of 'multiline' after stripping whitespace
print(len(multiline.lstrip()))  # Print the length after left-stripping whitespace
print(len(multiline.rstrip()))  # Print the length after right-stripping whitespace

# Build a Menu
title = "menu".upper()  # Convert "menu" to uppercase
print(title.center(20, "="))  # Center-align 'title' with '=' characters
print("Chaa".ljust(16, ".") + "$1".rjust(4))  # Create menu items with proper alignment
print("Biscuit".ljust(16, ".") + "$1".rjust(4))
print("JOL".ljust(16, ".") + "$1".rjust(4))

# String index Value
print(first[1])  # Print the second letter of 'first' (index starts at 0)
print(first[-1])  # Print the last character of 'first'
print(first[1:-1])  # Print characters from index 1 to the second-to-last character
print(first[1:])  # Print characters from index 1 to the end

# Some methods return boolean Data
print(first.startswith("P"))  # Check if 'first' starts with "P"
print(first.endswith("z"))  # Check if 'first' ends with "z"

# Boolean Data Type (Working With True and False)
myvalue = True  # Assign the boolean value True to 'myvalue'
x = bool(False)  # Create a boolean variable 'x' with the value False
print(type(x))  # Print the data type of 'x' (should be bool)
print(isinstance(myvalue, bool))  # Check if 'myvalue' is of boolean type

# Numeric data types

# Integer type
price = 100  # Assign the integer value 100 to 'price'
best_price = int(80)  # Convert the integer 80 to an integer
print(type(price))  # Print the data type of 'price' (should be int)
print(isinstance(best_price, int))  # Check if 'best_price' is of integer type

# Float Types
gpa = 3.28  # Assign the float value 3.28 to 'gpa'
y = float(1.14)  # Create a float variable 'y' with the value 1.14
print(type(gpa))  # Print the data type of 'gpa' (should be float)

# Complex Types
comp_value = 5 + 3j  # Assign a complex number (5 + 3j) to 'comp_value'
print(type(comp_value))  # Print the data type of 'comp_value'
print(comp_value.real)  # Print the real part of 'comp_value'
print(comp_value.imag)  # Print the imaginary part of 'comp_value'

# Built-in Functions for numbers

print(abs(gpa))  # Print the absolute value of 'gpa'
print(abs(gpa * -1))  # Print the absolute value of the negation of 'gpa'
print(round(gpa))  # Round 'gpa' to the nearest integer

print(round(gpa, 1))  # Round 'gpa' to one decimal place

print(math.pi)  # Print the value of pi from the math module
print(math.sqrt(64))  # Print the square root of 64
print(math.ceil(gpa))  # Round 'gpa' up to the nearest integer
print(math.floor(gpa))  # Round 'gpa' down to the nearest integer

# Casting a string to a Number
zipcode = "10001"  # Assign the string "10001" to 'zipcode'
zip_value = int(zipcode)  # Convert 'zipcode' to an integer
print(type(zip_value))  # Print the data type of 'zip_value'

# Error if attempting to convert a non-numeric string
# zip_value = int("Siliguri")
# This line would cause an error because "Siliguri" is not a valid integer.
