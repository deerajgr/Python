"""class Test(object):
    def __init__(self):
        print("I am constructor")
        print("Database connection")  
    def w(self):
        print("Withdraw")
    def d(self):
        print("Deposit")
    def m(self):
        print("Mini Statement")
x=Test()
x.w()
x.d()
x.m()
#----------------------------------------------------------------------------------------------------------------------------------------------
"""

"""import sys
sys.stdout.reconfigure(encoding='utf-8')

class ATM:
    def __init__(self, balance):
        self.balance = balance
        print(f"ATM initialized with balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")
        self.check_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: ₹{amount}")
            self.check_balance()

x = ATM(5000)
x.check_balance()
x.deposit(3000)
x.withdraw(400)
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
"""#single inheritance
class father:
    money=1000
    def show(self):
        print("Father class")
class son(father):
    def disp(self):
        print("Child class")
x=son()
x.show()
x.disp()
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
#Multilevel inheritance
class father():
    money=12000
    def showF(self):
        print("Father class")
class son(father):
    def showS(self):
        print("Son class")
class grandson(son):
    def showG(self):
        print("Grandson class")
x=grandson()
x.showF()
x.showS()
x.showG()
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
"""
#abstract class
from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def show(self):
        pass
    def showf(self):
        print("Father class")
class Son(Father):
    def shows(self):
        print("Son class")
class Grandson(Son):
    def show(self):  # Required implementation
        print("Implemented show() in Grandson")
    def showg(self):
        print("Grandson class")
x=Grandson()
x.shows()
x.showf()
x.showg()
x.show()
"""
"""
from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass #abstract class
    def show(self):
        print('Concrete Method')
class Child(Father):
    def disp(self):
        print("Defining Abstract Method")
c=Child()
c.disp()
c.show()
list duplicates and ordered we have to use
set no duplicates mutable 

"""
"""
a=[10,20,30,40,50,'list','code']
for i in a:
    print(i)
a[1] =5555
print(a)"""
"""
set1={30,40,44,40,50,50}
set1.add={30,43}
set1
print(set1)
"""
"""
d={}
stu={101:"Rahul",102:"Sam",103:"Sonam"}
fees=('rahul:100100)
print(stu)
--create display raise exit--
thank you for using the application
1)enter the name
enter the age
enter the designation
programmer manager tester(p 25 k/m 30 k/t20 k)(Y/N)
2)DISPLAY NAME AGE SALARY DESIGNATION

"""
"""
# Function to get employee input
def get_employee_input():
    name = input("Enter name: ")
    age = input("Enter age: ")
    designation = input("Enter designation (programmer/manager/tester): ").lower()
    return name, age, designation

# Function to validate designation and get salary
def get_salary(designation):
    salary_structure = {
        'programmer': 25000,
        'manager': 30000,
        'tester': 20000
    }
    if designation in salary_structure:
        return salary_structure[designation]
    else:
        return None

# Function to display employee details
def display_employees(employee_list):
    print("\nEmployee Details:")
    for emp in employee_list:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Designation: {emp['designation'].capitalize()}, Salary: ₹{emp['salary']}")

# Main function to run the program
def main():
    employee_list = []

    while True:
        name, age, designation = get_employee_input()
        salary = get_salary(designation)

        if salary is None:
            print("Error: Invalid designation. Please enter programmer, manager, or tester.")
            continue

        employee_list.append({
            'name': name,
            'age': age,
            'designation': designation,
            'salary': salary
        })

        cont = input("Do you want to add another employee? (yes/no): ").lower()
        if cont != 'yes':
            break

    display_employees(employee_list)

# Run the program
main()
"""