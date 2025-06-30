"""
try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    d = a / b
    print(d)
    print("Inside try")
except ZeroDivisionError:
    print("Division by zero is not allowed")
print("Rest of the code")
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    d = a / b
    print(d)
    print("Inside try")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Inside Else")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    d = a / b
    print(d)
    print("Inside try")
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Inside Else")
finally:
    print("Inside Finally")
#------------------------------------------------------------------------------------------------------------------------------------------------------------    
"""
"""
a=10
b=4
try:
    d = a / b
    print(d)
    print("Inside try")
except (NameError,ZeroDivisionError) as obj:
    print(obj)
print("Rest of the code")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input("Enetr Age:"))
if age<60:
    raise TooYoungException("Plz wait some more time you will get best match soon!!!")
elif  age>18:
    raise TooOldException("Your age already crossed marriage age...no change og getting")
else:
    print("You will get match details soon by email !!!")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

try:
    age = int(input("Enter Age: "))
    if age < 18:
        raise TooYoungException("Please wait, you're too young for marriage!")
    elif age > 60:
        raise TooOldException("Sorry, you have crossed the typical marriage age.")
    else:
        print("You will get match details soon by email!")
except TooYoungException as e:
    print(f"TooYoungException: {e.msg}")
except TooOldException as e:
    print(f"TooOldException: {e.msg}")
#------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
f=open('student.txt',mode='w')
f.write('Hello\n')
f.write('Python Training\n')
f.write('How are you\n')
f.close()
print("Writing Success")
f=open('student.txt',mode='a')
name = input("Enter the name of the employee: ") 
age = int(input("Enter the age of the employee: ") )
f.write(name+'\n')
f.write(age+'\n')
print("Data is written")
f=open('student.txt',mode='r')
print(f.readlines())
f.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
1)create 
2)display
3)raise salary
4)exit

1)enter your Name
2)enter your Age (18-60)
3)enter your Designation(P25/M30/T20) Y/N

2)Name age salary designation
3)raise salary
   enter the name of the employee stored in File 
   how much percentage hike (max 30%)
4)thank you using application
   
"""