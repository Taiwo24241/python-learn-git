import random
def transport():
    print ("Welcome to my Ease transport service")
    menu = input("Enter 1. TO visit the bank 2. To use our transport service: ")
    if menu == "1":
        my_bank.reception()
    elif menu == "2":
        card_num = input("Enter your card number: ")
        card_pin = input("Enter your card pin: ") 
        verify_card = my_bank.verify_card(card_num, card_pin)
        if verify_card:
            print("You have boarded the bus. Thanks for using our transport service.")
        else:
            print("Incorrect input.")

        print("Would you like to do anything else? ")
        repeat = input("1. Yes 2. No: ")
        if repeat == "1":
            transport()
        else:
            print("Bye!")




class Card():
    def __init__(self, firstname, lastname, pin, num ):
        self.firstname = firstname
        self.lastname = lastname
        self.pin = pin
        self.num = num
        print(f"Dear {self.firstname}, your card has been created successfully.")
        print(f"Here is your Card number: {self.num}")

class Bank:
    def __init__(self, name):
        self.name = name
        self.cards = {}

    def make_card(self):
        firstname = input("enter your firstname: ")
        lastname = input("Enter your lastname: ")
        card_num = random.randint(10 ** 10, 10 ** 11 - 1)
        pin = int(input("Enter your pin: "))
        repeat_pin = int(input("Enter your pin again: "))
        if pin == repeat_pin:
            new_card = Card(firstname=firstname, pin=pin, lastname=lastname, num=card_num)
            self.card[card_num] = new_card 
        else:
            print("The pin do not match")

    def reception(self):
        print("Welcome. What would you like to do? ")
        bank_menu = input("1. Generate card: ")
        if(bank_menu == "1"):
            self.make_card()

    def verify_card(self, num, pin):
        if num in self.cards:
            if self.cards[num].pin == pin:
                print("Card verified successfully")
                return True
            else:
                print("Incorrect card pin.")
                return False
        else:
            print("Card does not exist")


# class MyTransportService:
#     def __init__(self, name):
#         self.name = name
#         self.buses = {}
#     def add_bus(self, num, name, driver):
#         name = input("Enter the name of the bus.")
#         driver = input("Enter the driver's name")
#         num = random.randint(10**10, 10** 11 - 1)
#         new_bus = {"name": name, "driver": driver, "num": num}
#         self.buses[num] = new_bus

my_bank = Bank("python")
transport()