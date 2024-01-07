### Exercise 1: Names 

#Store the names of a few of your friends in a list called names. Print 
#each person’s name by accessing each element in the list, one at a time.

names = ["Kent", "Jerome", "Raven"]
print(names[0])
print(names[1])
print(names[2])



### Exercise 2: Greetings 

names = ["Kent", "Jerome", "Raven"]
message = "You have a nice name, "
print(message + names[0] + "!")
print(message + names[1] + "!")
print(message + names[2] + "!")




### Exercise 3: Your Own List 

transpo = ["car", "Trains", "Walking"]
print("I would like a reliable " + transpo[0] + ".")
print(transpo[1] + " are an efficient mode of transportation.")
print(transpo[2] + " is one way to stay physically fit.")




### Exercise 4: Guest List 
#If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d
#like to invite to dinner. Then use your list to print a message to each person, invitingthem to dinner.


guests = ["Einstein", "DeGrasse Tyson", "Steve Jobs"]
inv_msg = ", you are hereby invited to my 'Greatest Minds' dinner."
print(guests[0] + inv_msg)
print(guests[1] + inv_msg)
print(guests[2] + inv_msg)




### Exercise 5: Change Guest List 

guests = ["Einstein", "DeGrasse Tyson", "Steve Jobs"]
inv_msg = ", you are hereby invited to my 'Greatest Minds' dinner."
print(guests[0] + inv_msg)
print(guests[1] + inv_msg)
print(guests[2] + inv_msg)
print(guests[0] + " cannot make it to the dinner.")

guests[0] = "Jane Goodall"
print(guests[0] + inv_msg)
print(guests[1] + inv_msg)
print(guests[2] + inv_msg)




### Exercise 6: Shrinking Guest List 

guests = ["Jane Goodall", "DeGrasse Tyson", "Steve Jobs"]
print("Due to unforseen circumstances, I can only accomodate two people into my 'Greatest Minds' dinner.")
removed_guests = guests.pop()
print("We regret to inform you " + removed_guests + ", that we cannot accomodate you in our Greatest Minds dinner.")

confirm_msg = ", you are still invited to our 'Greatest Minds' dinner."
print(guests[0] + confirm_msg)
print(guests[1] + confirm_msg)

del guests[]
print(guests)




## Exercise 7: Seeing the World

travel = ["Germany", "Switzerland", "Cape Canaveral", 
          "Stonehenge", "California"]
print(travel)

print(sorted(travel))
print(travel)

print(sorted(travel,reverse=True))
print(travel)

travel.reverse()
print(travel)

travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse=True)
print(travel)







