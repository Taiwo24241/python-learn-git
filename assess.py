#assignment
actual_num = int(input("Enter a number: "))
guessed_num = int(input("Guess the actual number: "))
#if wrong then give a hint 
while guessed_num != actual_num:
    if guessed_num < actual_num:
        print("Move Higher")
    elif guessed_num > actual_num:
        print("Move Lower")
    guessed_num = int(input("Guess number again: "))
else:
    print("Correct")