print("welcome to TMO Bank")
user_acct_bal = 50000
bank_users = []
def bank():
    menu = input("Click 1. To open account 2. To login 3. To print all user info 4. To exit: ")
    if(menu == "1"):
        open_acct()
    elif(menu == "2"):
        to_login()
    elif(menu == "3"):
        print(bank_users)
    elif(menu == "4"):
        print("Thank you for banking with us!")
    print("Do you want to do any other thing?")
    repeat = input("1. Yes 2. No: ")
    if(repeat == "1"):
        bank()
    else:
        print("Thank you for banking with us")

def open_acct():
    global user_acct_bal
    user_f_name = input("Enter your firstname: ")
    user_l_name = input("Enter your lastname: ")
    user_email = input("Enter your email address: ")
    user_password = input("Enter password: ")
    if(len(user_password) < 8):
        print("Password must contain up to 8 words")
        user_password = input("Re-enter passsword: ")
    import random
    acct_num = (random.randint(10**9, 10**10-1))
    print(f"{user_f_name} {user_l_name} your account number is {acct_num}")
    user_details = {"firstname": user_f_name, "lastname": user_l_name, "email": user_email, "password": user_password, "acctnumber": acct_num}
    bank_users.append(user_details)

def to_login():
    user_email = input("Enter your email address: ")
    user_password = input("Enter password: ")
    user_found = None
    for user in bank_users:
        if user["email"] == user_email and user["password"] == user_password:
            user_found = user
            break

    if user_found:
        print(f"Welcome, {user_found["firstname"]} {user_found["lastname"]}! you have {user_acct_bal} in your account")
    anyother_thing = input("Enter 1. To do any other thing 2. To logout: ")
    if(anyother_thing == "1"):
        print("Hi")
    elif(anyother_thing == "2"):
        bank()
    else:
        print("Invalid email or password!")
        to_login()
    
bank()
# import random
# print(random.randint(10**9, 10**10-1))