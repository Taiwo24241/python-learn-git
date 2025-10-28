print ("TIP CALCULATOR")
def tip():
    amt_purchased = float(input("What is the total amount of things you purchased? "))
    tip_percen = float(input("What is the tip percentage you are willing to give? "))
    total_bill = amt_purchased + ( tip_percen / 100 * amt_purchased)
    print(total_bill)
    repeat = input("Do you want to go again? 1. Yes 2. No ")
    if(repeat == "Yes"):
        tip()
    else:
        print("BYE!")
tip()