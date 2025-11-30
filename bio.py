print("Welcome to your student bio data")
data = {}
def bio():
    details = int(input("Enter; 1. To add new data 2. To see data values 3. To see all data info 4. To clear all information: "))
    if (details == 1):
        new_data = input("Enter the key: ")
        new_data_value = input(f"Enter the value for {new_data}: ")
        data[new_data] = new_data_value
        print(f"{new_data} successfully entered")
    elif (details == 2):
        print(data.values())
    elif (details == 3):
        print(data)
    elif (details == 4):
        print(data.clear())


    another_entry = input("Do you want to do anything else? Y / N: ")
    if (another_entry == "Y"):
        bio()
    else:
        print("Bye!")


bio()
