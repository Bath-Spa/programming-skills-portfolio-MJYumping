### Exercise 1: Person :ballot_box_with_check:

person_info = {
    "first_name": "Jerome",
    "last_name": "Smith",
    "age": 18,
    "city": "Manila"
}
for key, value in person_info.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n")


### Exercise 2: Glossary :ballot_box_with_check:

glossary = {"variable": "represents a value",
            "string": "a collections of characters",
            "print": "used to display data as output on screen",
            "concatenation": "data that is joined together from previous lines of code",
            "loop": "tasks that the computer repeats for a given amount of times"
}
for key, value in glossary.items():
    print(key)
    print("\t"+value+"\n")



### Exercise 3: Glossary 2 :ballot_box_with_check:

print(glossary["variable"])
print(glossary["string"])
print(glossary["print"])
print(glossary["concatenation"])
print(glossary["loop"])

glossary = {"variable": "represents a value",
            "string": "a collections of characters",
            "print": "used to display data as output on screen",
            "concatenation": "data that is joined together from previous lines of code",
            "loop": "tasks that the computer repeats for a given amount of times",
}
glossary2 = {"boolean": "stores values that are either true or false",
            "dictionary": "a collection of key-value pairs",
            "list": "a collection of elements of any data types",
            "programming language": "human understandable language used to give a computer instructions",
            "integer": "a numerical value without a decimal point"
}

glossary.update(glossary2)

for key, value in glossary.items():
    print(key)
    print("\t"+value+"\n")

print("\n")






### Exercise 4: Rivers :ballot_box_with_check:

#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

#* Use a loop to print the name of each river included in the dictionary.

#* Use a loop to print the name of each country included in the dictionary.

rivertocountry = {"Nile River": "Egypt",
                "Mississipi River": "United States of America",
                "Cagayan River": "Philippines"
}
for key, value in rivertocountry.items():
    print(f"The {key} runs through {value}.")

print("\n")

for key in rivertocountry.keys():
    print(key)

print("\n")

for value in rivertocountry.values():
    print(value)





### Exercise 5: Pets :ballot_box_with_check:

#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

#each pet


pet1 = {"Species": "Hamster", "Age": "1 Year Old", "Owner": "Jerome"}
pet2 = {"Species": "Dog", "Age": "2 Years Old", "Owner": "Kent"}
pet3 = {"Species": "Cat", "Age": "6 Years Old", "Owner": "MJ"}
pet4 = {"Species": "Iguana", "Age": "10 Years Old", "Owner": "Mike"}


print("\n")


pets = [pet1, pet2, pet3, pet4]

for ptd in pets:
    print(ptd)