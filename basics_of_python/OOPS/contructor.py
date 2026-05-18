# What is a Constructor?
'''
A constructor is a special method that is automatically called when an object is created. 
It is used to initialize the object's attributes.


Constructors in Python
├── 1. Default Constructor
├── 2. Non-Parameterized Constructor
└── 3. Parameterized Constructor


'''
# class Car:
#     def __init__(self):      # ← This is the constructor
#         print("Object Created!")

# c = Car()    # Output: Object Created!  ← auto called, you didn't call __init__ manually

'''


class Employee:
    def __init__(self, name, dep, salary):
        self.name = name
        self.dep = dep
        self.salary = salary
        
    def showInfo(self):
        return f"Name: {self.name} | Dep: {self.dep} | Salary: {self.salary}" 


E1 = Employee("vijay", "computer", 35000)
print(E1.showInfo())     


'''



class Student:
    def __init__(self, *args):
        self.students = list(args)
    
    def showStudent(self):
        count = 1
        
        for i in  self.students:
            print(f"{count} student  :  {i}")
            count =  count + 1


stud = Student("vijay", "amol","tejas", "kanif")
stud.showStudent()

                