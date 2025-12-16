# try:
#     num = int(input("Enter a number: "))
#     print(num + 5)
# except Exception as e:
#     print("Something went wrong", e)
# # else: 
# #     print("Everything was excuted succefully")
# finally:
#     print("I will always be executed")


# try:
#     print("Hello")
#     print(a)
#     print(5 / 0)
# except NameError:
#     print("undefined variable")
# except ZeroDivisionError:
#     print("Cannot divide by 0")

#Error Class
class AgeError(Exception):   #the error class will an extension of exception
    def __init__(self, age):
        self.age = age
        super().__init__(age)

def handle_age(age):
    if age < 0:
        raise AgeError(age)
    
try:
    age = int(input("Enter your age: "))
    handle_age(age)
except AgeError as e:
    print("Age error executing", e)

# try:
#     age = int(input("Enter you age: "))
#     if age < 0:
#         raise AgeError("Age cannot be less than 0.")
# except Exception as e:
#     print("Something went wrong")