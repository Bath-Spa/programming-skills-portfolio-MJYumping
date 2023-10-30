####Program samples (from powerpoint)
### Program 7
# Python code using stripping

# string
a = "\tMJ Yumping\n"
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

enter_space = " \n"
print(enter_space)

### Program 9
#Write a python program that calculates how many candies he can buy and how many dollars he will have left.
#Total dollar = 20$
#Each candy = 2$

# Python code that calculates how many candies he can buy and how many dollars he will have left.
candies_bought = ("Total candies bought are = ")
money_left = "Total money that is left = "
print(candies_bought + str(int(20/2)))
print(money_left + str(20%2))