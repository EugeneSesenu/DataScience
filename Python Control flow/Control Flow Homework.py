"""Exercise 1
   Guess a number between 1 to 9 given by the user""" 
   
guess = int(input("guess a number between 1 to 9: "))
if 1<guess < 9:
        #print("right guess")
else:
        #print("wrong guess")
        
        


"""Exercise 2 
Exercise 2
Check the validity of password input by the user.

Validation:

At least 1 letter between [a-z] and 1 letter between [A-Z]
At least 1 number between [0-9]
At least 1 character from [$#@]
Minimum length 6 characters
Maximum length 16 characters """





def validate_password():
    symbol = ["$", "#", "@"]
    password = input("What is your password:")
    chec = True
    
    if len(password) < 6:
        print("password has to be at least 6 characters")
        chec = False 
    if len(password) > 16:
        print("password has to be less than 16 characters")
        chec = False 
    if not any(char in symbol for char in password):
        print("password should contain at least 1 symbol")
        chec = False
    if not any(char.isdigit()for char in password):
        print("password should contain at least 1 number")
        chec = False 
    if not any(char.isupper() for char in password):
        print("password should contain at least 1 uppercase letter")
        chec = False
    if not any(char.islower() for char in password):
        print("password has to contain at least 1 lowercase letter")
        chec = False 
    if chec:
        print("This is a good password")



"""Exercise 3 
Get input of the age of 3 people by user and determine oldest and youngest among them """

dict = {"Person1: Eugene", "Person2: Steff", "Person3: Klaus"}


person1 = int(input("Person1 age:"))
person2 = int(input("Person2 age:"))
person3 = int(input("wPerson3 age:"))
ages = [person1, person2, person3]   

if   person1 is max(ages):
     print("Eugene is  the oldest")
elif person2 is max(ages):
     print("Steff is the oldest")
elif person3 is max(ages):
     print("Klaus is the oldest")
    
if   person1 is min(ages):
     print("Eugene is the youngest")
elif person2 is min(ages):
     print("Steff is the youngest")
elif person3 is min(ages):
     print("Klaus is the youngest")

"""Exercise 4
A student will not be allowed to sit in exam if his/her attendance is less than 75%.

Take following input from user

Number of classes held
Number of classes attended.
And print
percentage of class attended"""

def attendance():
    classesheld  = int(input("How many classes were there:"))
    classespresent = int(input("How many classes did you attend:"))
    percentage = (classespresent/classesheld) * 100
    if percentage < 75:
        print("You will not be allowed to take the exam")
    else:
        print("You will be allowed to take the exam")
        
        
        
    







"""Exercise 5
Get an integer N from the user and perform the following actions:

if N is odd, print "weird"
if N is even and in the inclusive range of 2 to 5, print "Not Weird"
if N is even and in the inclusive range of 6 to 20, print "Weird"
if N is even and greater than 20, print "Not Weird" """

def integer():
    Integer = int(input("enter an integer: "))
    
    if (Integer % 2) != 0:
        print("weird")
    elif (Integer % 2) == 0 and 2<Integer<5:
        print("Not Weird")
    elif (Integer % 2) == 0 and 6<Integer<20:
        print("Weird")
    elif (Integer % 2) == 0 and Integer>20:
        print("Not Weird")





















