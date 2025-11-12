#assignment
# actual_num = int(input("Enter a number: "))
# guessed_num = int(input("Guess the actual number: "))
# #if wrong then give a hint 
# while guessed_num != actual_num:
#     if guessed_num < actual_num:
#         print("Move Higher")
#     elif guessed_num > actual_num:
#         print("Move Lower")
#     guessed_num = int(input("Guess number again: "))
# else:
#     print("Correct")


#assignment 2
# start_point = int(input("Enter a starting point:  "))
# end_point = int(input("Enter the end point: "))
# skip_num = int(input("Enter the number you want to skip: "))
# actual_num = start_point
# while actual_num <= end_point:
#     if actual_num != start_point:
#         print(actual_num)
#     actual_num = actual_num + 1

start_point = int(input("Enter a starting point:  "))
end_point = int(input("Enter the end point: "))
skip_num = int(input("Enter the number you want to skip: "))
for point in range(start_point, end_point):
    if point == skip_num:
        continue
    print(point)