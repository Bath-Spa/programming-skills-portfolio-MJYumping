
### Exercise 1: Variables
# Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.

# This assigns the first message to the variable "msg1" and then prints that message
msg1 = "Hello, I am the computer!"
print(msg1)

# This changes the value of variable "msg1" and then also prints that message.
msg1 = "I am actually a donut."
print(msg1)





### Exercise 2: Variables
#Find a quote from a famous person you admire. Print the quote and the name of its author.

q1 = 'Stephen Hawking once said, "The greatest enemy of knowledge is not ignorance,\nit is the illusion of knowledge.'
print(q1)





### Exercise 3: Stripping Names

name1 = "\tStephen Hawking\n"
print(name1)
print(name1.lstrip())
print(name1.rstrip())
print(name1.strip())





### Exercise 4: Favorite Number
# Use a variable to represent your favorite number. Then using that variable, 
# create a message that reveals your favorite number. Print that message.

fnum = 4
print("My favourite number is:", fnum)





### Exercise 5: USB Shopper
# Write a programme that calculates how many USB sticks
# she can buy and how many pounds she will have left.
# Total dollars = 50
# Each USB = 6

USBbought = ("Total USBs bought are = ")
dollars_left = ("Total money left is = ")

print(USBbought + str(int(50/6)))
print(dollars_left + str(50%6))





#### Powerpoint program samples
### Program 7
# Python code using stripping

# string
a = "\tMJ Yumping\n"
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())




### Program 9
#Write a python program that calculates how many candies he can buy and how many dollars he will have left.
#Total dollar = 20$
#Each candy = 2$

# Python code that calculates how many candies he can buy and how many dollars he will have left.
candies_bought = ("Total candies bought are = ")
money_left = "Total money that is left = "
print(candies_bought + str(int(20/2)))
print(money_left + str(20%2))