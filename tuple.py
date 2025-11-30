# names = ("Tolu", "Ade", "Aina")
# print(name[0])
# for name in names:
#     print(f"my name is {name}")
# name.pop() ----- you cannot pop, remove or add. generally, you cannot make changes

# student = {"name": "Taye", "dept": "CSC"}
# for (x, y) in student.items():
#     print(f"The key is {x} and the value is {y}")

# To make changes in a tuple, convert to another data type then convert it back to a tuple
names = ("Tolu", "Ade", "Aina")
new_names = list(names) # convert to a list to make changes then convert back to tuple
new_names[0] = "ola"
print(new_names)
names = tuple(new_names)
print(names)

#To count the number of items in a tuple
print(names.count("Ade"))