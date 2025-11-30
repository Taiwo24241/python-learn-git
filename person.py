print("Welcome")
Everyone = []
def start_work():
    print("What do you waht to do")
    menu = input("1. Add new person 2. To get oldest person 3. Average age 4. To greet everyone 5. Edit person 6. Delete person: ")
    if (menu == "1"):
        add_new_person()
    elif (menu == "2"):
        get_oldest()
    elif (menu == "3"):
        get_average_age()
    elif (menu == "4"):
        greet_everyone()
    elif (menu == "5"):
        edit_person()
    elif (menu == "6"):
        delete_person()
    print("Do you want to do anything else? ")
    another_thing = input("Enter 1. Yes 2. No: ")
    if (another_thing == "1"):
        start_work()
    else: 
        print("BYE!!!")

        



def add_new_person():
    f_name = input(" Enter the firstname: ")
    l_name = input(" Enter the last name: ")
    user_age = int(input(" Enter the age: "))
    new_person = {"firstname": f_name, "lastname": l_name, "age": user_age}
    Everyone.append(new_person)
    print(f"{f_name} {l_name} added successfully.")

def get_oldest():
    oldest = 0
    oldest_person = {}
    for person in Everyone:
        current_age = person["age"]
        if (current_age > oldest):
            oldest = current_age
            oldest_person = person
    print(f"{oldest_person["firstname"]} {oldest_person["lastname"]} is the oldest with the age of {oldest}")

def get_average_age():
    total_persons = len(Everyone)
    total_age = 0
    for person in Everyone:
        current_age = person["age"]
        total_age = total_age + current_age
    average_age = total_age / total_persons
    print(f"The average age of everyone is {average_age}")

def greet_everyone():
    for person in Everyone:
        print(f"Good Morning {person["firstname"]} {person["lastname"]}")

def edit_person():
    index = int(input("Enter the index you want to edit: "))
    key = input("Enter the key you want to edit: ")
    value = input(f"Enter the value for {key}: ")
    Everyone[index][key] = value
    print(f"{key} edited successfully")

def delete_person():
    index = int(input("Eneter the index you want to delete: "))
    person = Everyone[index]
    del Everyone[index]
    print(f"{person["firstname"]} deleted successsfully")


start_work()