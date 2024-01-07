### Exercise 1: Pizza Toppings :ballot_box_with_check:

topping = input("Enter an example of a pizza topping, enter 'quit' when you are done: ")

while topping != "quit":
  print("I will add", topping, "as topping to your pizza.\n")
  topping = input("Enter another example of a pizza topping, enter 'quit' when you are done: ")
else:
  print("\n")



### Exercise 2: Movie Tickets: :ballot_box_with_check:

age = int(input("What is your age?  "))

if age < 3:
  print("As you are", age, "years old, your ticket will be FREE.\n")
elif 3 <= age <= 12:
  print("As you are", age, "years old, your ticket will cost $10.\n")
else:
  print("As you are", age, "years old, your ticket will cost $15.\n")



### Exercise 3: Infinity :ballot_box_with_check:

#num = 1

#while num != 0:
  #num = num + 1
  ##or num += num
  #print(num)



  

### Exercise 4: Deli :ballot_box_with_check:

sandwich_orders = ["Chicken", "Egg", "Grilled Cheese", "Ham"]
finished_sandwiches = []

print("Current Sandwich Orders:", sandwich_orders)
print("Now Serving:", finished_sandwiches, "\n")

while sandwich_orders:
  current_sorder = sandwich_orders.pop(0)
  print("Your order of", current_sorder, "sandwich is now served.")
  finished_sandwiches.append(current_sorder)

print("\nCurrent Sandwich Orders:", sandwich_orders)
print("Now Serving:", finished_sandwiches, "\n")




### Exercise 5: No Pastrami :ballot_box_with_check:

#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 

#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

newsandwiches = ["Grilled Cheese", "Pastrami", "Pastrami", "Pastrami"]
finished_sandwiches = []

print("The Deli has run out of Pastrami.\n")
print("Current Sandwich Orders:", newsandwiches)
print("Now Serving:", finished_sandwiches, "\n")

while "Pastrami" in newsandwiches:
 newsandwiches.remove("Pastrami")

while newsandwiches:
  current_sorder = newsandwiches.pop(0)
  print("Your order of", current_sorder, "sandwich is being prepared.")
  finished_sandwiches.append(current_sorder)

print("\n")

print("Current Sandwich Orders:", newsandwiches)
print("Now Serving:", finished_sandwiches, "\n")









