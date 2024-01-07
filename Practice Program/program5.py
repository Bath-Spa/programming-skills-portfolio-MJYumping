student = {"name": "alpha", "id": 5}
print(student["name"])
print(student["id"])


student = {"name": "alpha", "id": 5, "course": "BSC CC"}
print("Display key value pairs")
for key, value in student.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print("\nDisplay only keys")
for key in student.keys():
    print(key)

print("\nDisplay only values")
for value in student.values():
    print(value, "\n")

student = {"name": "alpha", "id": 5}
student["course"] = "BSC CC"
print(student)

student = {"name": "alpha", "id": 5, "course": "BSC CC"}
print("\nStudent Details before altering the value\n", student)
student["course"] = "BA B&M"
print("\nStudent details after altering the value\n", student)


student = {"name": "alpha", "id": 5, "course": "BSC CC"}
print("\n Student Details after deleting the value\n", student)
del student["course"] 
print("\n Student Details after deleting the value\n", student, "\n")


student1 = {"name": "alpha", "id": 5, "course": "BSC CC"}

student2 = {"name": "beta", "id": 10, "course": "BSC CC"}

student3 = {"name": "gamma", "id": 15, "course": "BA"}

student4 = {"name": "delta", "id": 20, "course": "BA"}

student = [student1, student2, student3, student4]
for std in student:
    print(std)


student = {
    "name": "alpha",
    "marks": ["Codelab1 - 78", "Codelab2 - 82"]
}

print(f"The student name {student['name']} scored the following marks:")
for mark in student["marks"]:
    print("\t" + mark)