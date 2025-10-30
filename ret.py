# Return function
# def double(val):
#      return val * 2

# a = double(10) 
# print(a)
# b = double(80)
# print(b)

def divideTwo(first, second):
    if(second != 0):
        return first / second
    else:
        print('You cannot divide by zero')

# a = divideTwo(50, 0)
# if(a == 100):
#     print("Success")
# else: 
#     print('Wrong')

b = divideTwo(8, 0)
if(b is None):
    print("Correct")
# def my_fun():
#     print("Hello")
#     return 7


# my_fun()
# a = my_fun()
# print(a)