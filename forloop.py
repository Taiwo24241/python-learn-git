# names = ["Taye", "Kehinde", "Idowu", 7, True, "Rukayat", "Taiwo"]
# print(len(names))
# for name in names:
#     print(name)
#     print("Hello")
#     print(f"heyyy! {name}")

# print(f"my name is {names[0]}")
# print(f"my name is {names[1]}")
# print(f"my name is {names[2]}")
# print(f"my name is {names[3]}")
# print(f"my name is {names[4]}")
# print(f"my name is {names[5]}")
# print(f"my name is {names[6]}")
# print(f"my name is {names[7]}")

# nums = [8, 12, 15, 6]
# print(total)
# total = 0
# for num in nums:
#     total = total + num #total = 35 + 6 = 41
#     print(total)
#     print(f"The sum of all the values in the list is {total}")



    #Assignment 
    #get the highest number in ths list [8, 12, 15, 6, 20, 6, 56, 1]
    # max(nums)

numbers = [8, 12, 15, 6, 20, 6, 56, 1]
highest_num = 0
for number in numbers:
    if number > highest_num:
        highest_num = number
print(highest_num)