# names = {"Tolu", "Ade", "Aina", "Ope"}
# print(names)

#list_of_dico assignment
print("Welcome tp Oasis college")
details = [
    
           
]
def school():
    bio_data = input("What do you want to do; 1. To add new student 2. To edit a student info 3. To delete a student info 4. To print all the students: ")
    if(bio_data == "1"):
        add_new_data()
        # key_name = input("Enter the key: ")
        # value_name = input("Enter the {key_name} of the student: ")
        # key_department = input("Enter the key: ")
        # value_department = input("Enter the {key_department} of the student: ")
        # new_details = {"{key_name}": "{value_name}", "{key_department}": "{value_department}"}
        # print("New student successfully added")
    elif(bio_data == "2"):
        edit_std_info()
        # std_index = int(input("Enter the index of the student: "))
        # edit_key = input("Enter the key you want to change: ")
        # new_edit_value = input("Enter the new value: ")
        # details[std_index][edit_key] = new_edit_value
        # print(f"{new_edit_value} changed successfully")
    elif(bio_data == "3"):
        delete_std_info()
        # del_details = int(input("which index do you want to delete? "))
        # del details[del_details]
        # print(f" {del_details} has been successfully deleted")
    elif(bio_data == "4"):
        print(details, '\n')

    print("do you want to do any other thing? ")
    repeat = input("Enter 1. Yes  2. No: ")
    if repeat == "1":
        school()
    else:
        print("BYE!")


def add_new_data():
    std_f_name = input("Enter your firstname: ")
    std_l_name = input("Enter your lastname: ")
    std_dept = input("Enter your dept: ")
    new_student = {"firstname": std_f_name, "lastname": std_l_name, "department": std_dept}
    details.append(new_student)
    print(f"{new_student["firstname"]} {new_student['lastname']} has been added successfully")

def edit_std_info():
    index = int(input("Enter the index you want to edit: "))
    key = input("Enter the key you want to edit: ")
    new_value = input(f"Enter the new {key}: ")
    details[index][key] = new_value
    print(f"{key} has been succefully changed")

def delete_std_info():
    index = int(input("Enter the index you want to delete: "))
    student = details[index]

    del [index]
    print(f"{student["firstname"]} {student["lastname"]} has been deleted successfully")


school()