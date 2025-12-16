# with open("assignment.txt", "r") as myfile:
# with open("bank.py", "r") as myfile:  #for .py file
# for image file include the encoding for the image e.g. with open("assignment.txt", "r", encoding"utf-g") as myfile:
    # print(myfile.read())

#To add or write text 
with open("assignment.txt", "w") as myfile:
    myfile.write("How are you doing?")  #it will replace the entire content in assignment.txt with "How are you doing?"
#use "a" to append instaed of replacing the entire content
with open("assignment.txt", "a") as myfile:
    myfile.write("\n How are you doing?")

#To check if a file exist
#import OS
import os
if os.path.exists("assignment.txt"):
    print("The file is present")
else:
    print("Assignment.txt is not here")

#To delete a file
import os
os.remove("dog.txt")