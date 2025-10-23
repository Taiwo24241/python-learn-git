print("Welcome to my calculator")
def calculator():
    menu = input("1. Add 2. Substraction 3. multiplication 4. div ")
    if(menu == "1"):
        add()
    elif(menu == "2"):
        sub()
    elif(menu == "3"):
        mul()
    elif(menu == "4"):
        div()
    else:
        print("Incorrect entry")
    print("Do you want to do any other thing? ")
    reload = input("1. yes 2. no ")
    if reload == "1":
        calculator()
    else:
        print("BYE!")

def add():
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    result = first + second
    print(result)
def sub():
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    result = first - second
    print(result)
def mul():
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    result = first * second
    print(result)
def div():
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    result = first / second
    print(result)
calculator()