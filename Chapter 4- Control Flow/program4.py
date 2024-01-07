## Exercise 1:  Alien Colors 

#Declaring an alien color variable to green
alien_color = "green"

#It will pass this test and will print a message
if alien_color == "green":
    print("Player earned 5 points!")

#This will fail the test condition as the variable does not satisfy the condition
alien_color = "yellow"

if alien_color == "green":
    print("Player earned 5 points!")





### Exercise 2: Alien Colors #2 

#This will run the if block as the alien color matches with the condition
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points from shooting that alien!")
else:
    print("You just earned 10 points!")


#This will skip IF block and run ELSE block as the variable does not match with the if condition
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points from shooting that alien!")
else:
    print("You just earned 10 points!")







## Exercise 3: Alien Colors #3 :ballot_box_with_check:

#This will pass the if block and print 5 points
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


#This will pass the elif block and print 10 points
alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


#This will pass the else block and print 15 points
alien_color = "red"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")







### Exercise 4: Stages of Life

#Establishes the variable to be tested in the if-elif-else chain
age = int(input("What is your age?  "))

#This chain tests the value of the inputted number and prints the 
#message of the satisfied condition
if (age < 2):
    print("You are a baby!")
elif (2 <= age < 4):
    print("You are a toddler!")
elif (4 <= age < 13):
    print("You are a kid then!")
elif (13 <= age < 20):
    print("You're a teenager then!")
elif (20 <= age < 65):
    print("You are an adult.")
else:
    print("You are an elder.")







## Exercise 5: Favorite Fruit

#This code will declare the list of my favorite fruits, and put them in a variable.
favorite_fruits = ["apple", "mango", "watermelon"]


#The first three if blocks succeed because the condition is satisfied, and they will print the appropriate messages.
if "apple" in favorite_fruits:
    print("Apples grow on trees you know!")


if "mango" in favorite_fruits:
    print("I like mangoes too!")


if "watermelon" in favorite_fruits:
    print("Watermelons are very expensive!")


#The last two chains will fail and skip the if block and will instead print an alternative message located 
#in the else block because the fruit mentioned in the condition statement is not present in the list.
if "orange" in favorite_fruits:
    print("Oranges are difficult to eat.")
else:
    print("Oranges are not one of your favorite fruits.")


if "banana" in favorite_fruits:
    print("Bananas a monkey's favorite food.")
else:
    print("You dont like bananas.")













