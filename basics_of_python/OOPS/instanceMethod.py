
class Man:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
        
    
    def getInfo(self):
        return f"Name is {self.name}, and age is : {self.age}"



obj = Man("vijay", 26)
print(obj.getInfo())        


# Notes 

'''

1. Instance Methods (the default)
The regular method — always receives self (the instance).

'''


'''

class practice: 
    name = "vijay"
    
    def __init__(self,age):
        self.age = age
        
    def getInfo(self):
        print(f"name is: {practice.name}, and age is : {self.age}")
        
obj =  practice(26)
obj.getInfo()



self.age → comes from object
self.name → comes from class (if not in object)
Practice.name → directly from class


'''