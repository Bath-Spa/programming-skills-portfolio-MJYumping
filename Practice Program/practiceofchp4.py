print(42 == 42)

print(40 == 42)

print('hello' == 'hello')

print('hello' == 'Hello')

print('dog' != 'cat')

print(42 == 42.0)







print(1.0 > 0.75)

print(2 == 2.0 <1.5)

print(3 < 2 < "2")

print(1 < 2 < 3)

print(1 < 2 and 2 < 3)

#understand6 left to right
print(2 + 2 == 4  and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
# (true and not false and true)
# (true and true and true)
# (true and true)
# (true)

#understand7 left to right
print(5 > 4 or 3 < 4 and  5 > 5)
# (true or true and false)
# (true and false)
# (true)

grade = 95
print(100 >= grade >= 80)



response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")


lang = input("What's the programming language you want to learn?")

match lang:
    case "JavaScript":
        print("You can become a web developer")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")




product_code = input(str("Please input the 3 digit code of your chosen product:"))

match product_code:
    case "100":
        print("Your water bottle 500ml is now being dispensed, please enjoy.")
    case "101":
        print("Your orange juice 250ml is now being dispensed ")





student = {"name": "alpha", "id": 5}
print(student["name"])
print(student["id"])





