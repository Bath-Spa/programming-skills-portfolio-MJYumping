languages = ["Swift", "Python", "Go", "Javascript"]
for language in languages:
  print(language)


values = range(4)
for i in values:
  print(i)


languages = ["Swift", "Python", "Go"]
for language in languages:
  print("Hello")
  print("Hi\n")


digits = [0, 1, 5]
for i in digits:
  print(i)
else:
  print("No items left.")

  
total = 0
number = int(input("Enter a number:  "))
while number != 0:
  total += number
  number = int(input("Enter a number:  "))
print("total =", total)



num = 1

while num != 0:
  num += num
  print(num)






bouquet_orders = ["Wedding Bouquet", 
                  "Birthday Bouquet", 
                  "Party Bouquet", 
                  "Rose Bouquet"]

finished_order = []

while bouquet_orders:
  current_order = bouquet_orders.pop()
  print("I am working on your " + current_order + ".")
  finished_order.append(current_order)

print("\n")

for bouquets in finished_order:
  print("I made a " + bouquets + " bouquets.")










  