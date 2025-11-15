# for val in range(7):
#     print (f"i have {val} cars")
# names = ["Taye", "Kehinde", "Idowu"]
# # for name in names:
# #     print(name)
# for i in range(3): #0,1,2,3,4
#     print(names[i])

#or

# names = ["Taye", "Kehinde", "Idowu"]
# name_length = len(names)
# for i in range(name_length):
#     print(f"{names[i]} is at position {i}")

# Assignmet
names = ["Taye", "Kehinde", "Idowu", "Chioma" ]
name_len = len(names)
for name in range(name_len):
    if name != 2:
        print(f"my name is {names[name]}")

#Assignment 2
names = ["Taye", "Kehinde", "Idowu", "Taye", "Chioma" , "Taye"]
for i in names:
    if (i != "Taye"):
        print(i)