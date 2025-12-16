print("welcome to TMO Bank")
# user_acct_bal = 50000
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
    # global user_acct_bal
    user_f_name = input("Enter your firstname: ")
    user_l_name = input("Enter your lastname: ")
    user_email = input("Enter your email address: ").lower()
    for user in bank_users:
        if user["email"].lower() == user_email:
            print("Error: An account with this email already exist.")
            return
    user_password = input("Enter password: ")
    while (len(user_password) < 8):
        print("Password must contain up to 8 words")
        user_password = input("Re-enter passsword: ")
    import random
    acct_num = (random.randint(10**9, 10**10-1))
    print(f"{user_f_name} {user_l_name} your account number is {acct_num}")
    user_details = {"firstname": user_f_name, "lastname": user_l_name, "email": user_email, "password": user_password, "acctnumber": acct_num, "balance": 5000}
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
        print(f"Welcome, {user_found["firstname"]} {user_found["lastname"]}! you have {user_found["balance"]} in your account")
    

        print(" What will you like to do? ")
        activity_menu = input(" 1. Transfer 2. Check balance 3. Change info 4. Logout: ")
        if (activity_menu == "1"):
            transfer(user_found)
        elif (activity_menu == "2"):
            print(f"You have {user_found["balance"]} in your account")
        elif (activity_menu == "3"):
            edit_info(user_found)
        elif (activity_menu == "4"):
            bank()
        else:
            print("Invaild entry!")

def transfer(current_user):
    recipient_bank = input("Input recipient Bank: ")
    recipient_acct_num = int(input("Input recipient account number: "))
    trans_amount = float(input("Input amount: "))
    if trans_amount > current_user["balance"]:
        print("Insufficent balance")
        return 
    max_attempt = 3
    attempt = 0
    while attempt < max_attempt:
        user_password = input("Input your password: ")
        if user_password == current_user["password"]:
            current_user["balance"] -= trans_amount
            print(f"{trans_amount} has been successfully transferred to {recipient_acct_num}")
            # print("incorrect password, transaction has been cancelled!")
            break
        else:
            attempt = attempt + 1
            print(f" You have {max_attempt - attempt} attempts left.")
    else:
        print(" You have exceed your maximum password attempt. Transaction failed.")
        return
    # user_password = input("re-enter password: ") 
    
    
    
def edit_info(current_user):
    key = input("What field do you want to change? ")
    while key in ["email", "balance", "acct_num"]:
        print(f"You cannot change {key}!")
        key = input("Re-enter the field you want to change: ")
    if (key == "user_password"):
        new_password = input("Enter new password: ")
        while len(new_password) < 8:
            print(" Password length should be a minimum of 8 letters")
            new_password = input("Re-enter password: ")
    else: 
        new_value = input(f"Input the new {key}: ")
        if key in current_user:
            current_user[key] = new_value
            print(f"{key} has been changed successfully!") 
        else:
            print("Invalid field name")   
            
    #   else:
    #     print("Invalid email or password!")
    #     to_login()
    # anyother_thing = input("Enter 1. To do any other thing 2. To logout: ")
    # if(anyother_thing == "1"):
    #     print("Hi")
    # elif(anyother_thing == "2"):
    #     bank()
    
    
bank()
# import random
# print(random.randint(10**9, 10**10-1))