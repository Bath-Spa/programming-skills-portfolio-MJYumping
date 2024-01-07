### Exercise 1:   Message  :ballot_box_with_check:

def display_message():
    print("User-defined functions can make your program neat through modularizing.")

display_message()




print("\n")
### Exercise 2: Favorite Book :ballot_box_with_check:

def favorite_book(book_title):
    print("My favorite book is " + book_title + ".")

favorite_book("Moby Dick")



print("\n")
## Exercise 3: T-Shirt  :ballot_box_with_check:

#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

#arguments to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(size, mssg):
    print("The shirt with a size of " + size + " will have the message: " + mssg)

make_shirt("MEDIUM", "'Just Do It'")
make_shirt(size = "LARGE", mssg = "'Just Do It Tomorrow'")




print("\n")
## Exercise 4:  Large Shirts :ballot_box_with_check:

def make_shirt(size = "LARGE", mssg = "'I love Python'"):
   print("The shirt with a size of " + size + " will have the message: " + mssg) 

make_shirt()   
make_shirt(size = "MEDIUM")
make_shirt(size = "SMALL", mssg = "'Anyone Can Cook'")




print("\n")
## Exercise 5: Cities

def describe_city(city, country = "France"):
    print(city + "is a city in " + country + ".")

describe_city(city = "Paris ")
describe_city(city = "Tokyo ", country = "Japan")
describe_city(city = "Bath ", country = "England")

print("\n")