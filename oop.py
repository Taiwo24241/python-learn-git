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
