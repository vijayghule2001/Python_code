'''

1) What is self?
===> self is a reference to the current object (instance). It's automatically passed as the first argument to
any instance method — 
you don't pass it manually when calling.


'''

class Man:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        
    def printname(self):
        print(f"My name is {self.name} {self.lastname} ") 
    
    
obj = Man("vijay", "ghule")   
obj.printname() 
           