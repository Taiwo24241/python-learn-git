# object oriented programming
# object (properties (is more like variable) (describition of the object), 
# methods (it is more like function) (usefulness of the object))

# To create objects in bulk use class template
# the first letter after class (class name (Person))should start with capital letter

# class Person:
#     name = "patience"  #properties of class
#     hobby = "hike"  #properties of class

# first_person = Person() #to create an object from class, call on the class name. Save the object in a variable (first_person)
# print(first_person.name)
# print(first_person.hobby)
#python gives location of the object in memory when you print the whole object, just print what you need from the object eg print(a.name))

class Human:
    eyes = 2
    ears = 2
    head = 1
    def eat(self):   #method must have self in the parentheses, self is the first argument
        print("I am eating")
    
    def sleep(self, duration, side): #self refers to  the object calling on the function
        print(self.eyes)
        # print(f"I am having a good time sleeping for {duration}")

adam = Human()
eve = Human()
adam.eyes = 1
# print(adam.eyes)
# print(eve.eyes)
adam.sleep(8, "left")
eve.sleep(6, "right")


#Constructor
# The constructor is triggered immediately you create a new instance of a class
# constructor expects 2 arguments
# _init_ is the special method while _new_ crwates object instance, _new_ is a more advanced method
class person:
    def __init__(self, new_name, new_dept): 
        self.name = new_name
        print(self.name, self.dept)
        self.greet()  

    def say_hi(self):
        print(f"{self.name} How are you today? ")

    def greet(self):
        print("Good Evening Everyone")

a = person("Rukayat", "CSC")
a.say_hi()


# CLASS INHERITANCE 
# Allows new class (child class) to inherit attributes and methods from an existing class (parent class)
#  parent class or base class and child class or derived class
class human:
    eye = 2
    head = 1
    ears = 2
    def talk(self):
        print("I am talking")

    #To create a method taht displays and eye info
    def display_head_info(self):
        print(f" I have {self.eye} in my {self.head} head")

class man(human):
    # voice = "deep"
    # To make the voice dynamic
    # create a constructor first
    def __init__(self, voice, eye, head, ears):
        super().__init__(eye=eye, head=head, ears=ears)
        self.voice = voice
        #call on the parent constrctor
        
        

        super().__init__()
    def talk(self):  # method overriding 
        print("I am not talking")  # This talk will overide the talk above, it will print this *talk* for man instead of the one in human

class woman(human):
    hair = "plenty"
    def talk(self):
        super().talk() #super refers to the parent class
        print("I am not talking") # It will print the parent class " I am talking" first before printing this one
# adam = man(ears= 4, head= 1, eye= 2)
print(adam.eye)
adam.talk
adam.display_head_info


# Method Overriding
# Where a method overrides another method
