#creating a calculator
def calculate(val1, val2, opr):
    if(opr == "+"):
        return val1 + val2
    elif(opr == "-"):
        return val1 - val2
    elif(opr == "*"):
        return val1 * val2
    elif(opr == "/"):
        if(val2 == 0):
            print(f"You cannot divide {val1} by 0")
        else:
            return val1 / val2
print(calculate(5, 9, "+"))
print(calculate(3, 6, "*"))
print(calculate(12, 0, "/"))
