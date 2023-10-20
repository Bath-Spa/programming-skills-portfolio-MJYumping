### CHAPTER 1 Exercises

### EXERCISE 1: Print Strings
# Instruction: Write a Python program to print the following string in a specific format.

# I begin by assigning each line of the song with variables "a" to "f"
a = "Twinkle, twinkle, little star, "
b = "How I wonder what you are!" 
c = "Up above the world so high, "		
d = "Like a diamond in the sky."
e = "Twinkle, twinkle, little star, "
f = "How I wonder what you are."

# I then combine two consecutive lines and print them.
print(a + b)
print(c + d)
print(e + f)




### EXERCISE 2: Print the Version of Python
# Write a Python program to get the Python version you are using.

# First step is to import "sys" which will provide information about the python interpreter.
import sys

# Next step is to print the "sys.python" string which pulls the version of python from the sys module and note that this will not work if 'sys' is not defined.
print("The version of python installed is: "  + sys.version)




### EXERCISE 3: Print date and time
# Write a Python program to display the current date and time.

# Firstly we import the date and time using the program:
from datetime import datetime

# From that datetime module, we take the current date and time using "datetime.now()" and at the same time store it into a variable to print for later.
dnt = datetime.now()
print("The current date and time is: ", dnt)




### EXERCISE 4: Strings Concatination
# Write three strings in different variables and print the output as one string.

# First is to divide the final sentence output into 3 strings and assign each to a variable
str1 = "The cat was chasing a fox "
str2 = "whilst the lion looked on, amused "
str3 = "as he fell back asleep." 

# We then use print command and concatenate the three variables to display all strings into one continuous string/sentence.
print(str1 + str2 + str3)




### EXERCISE 5: Compute area of Circle
# Write a Python program which accepts the radius of a circle from the user and compute the area.

# First is to import the math library so that we can use the pi constant.
from math import pi

# Next we ask the user for a given radius of a circle (in integers) and at the same time placing it into a variable.
rad1 = int(input("Type a given radius of a circle and I will give you its area:"))

# Next we compute for the area of the circle with the proper formula and using the radius the user inputed. We then place the product into a variable.
radXpi = pi * rad1 ** 2

# Finally, we use the print function to display to the user the area of their circle together with the corresponding radius.
print("The area of a circle with a given circumference of", rad1, "is: ", radXpi)



