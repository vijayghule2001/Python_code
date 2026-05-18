class Employee:
    company = "NCPL" #class attributes
    work_hrs = 9 
    
    def __init__(self, name, position):
        self.name = name     #instance attributes 
        self.position = position
    
    def show(self):
        print(f"{self.name} |  {Employee.company} | {self.work_hrs} | {self.position}") 
           


E1 = Employee("vijay", "Jr softwar developer")
E1.show()    


Employee.company = "TCS"

E2 = Employee("kaka", "Jr softwar ")
E2.show()    
