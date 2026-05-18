# class staticMethod:
    
#     @staticmethod
#     def isPrime(num):
#         if num <= 1 :
#             return False
        
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
            
#         return True


# num = 7
# if staticMethod.isPrime(num):
#     print("Number is Prime ")
# else:
#     print("Number is not a Prime number")            
    
    

'''
@staticmethod is a built-in decorator used to define a method inside a class that does not 
require access to the class (cls) or the instance (self). It behaves like a regular function 
but is placed within the class for logical organizatio


Key Characteristics: 


No Implicit Arguments:  Unlike instance methods (which take self) or class methods (which take cls),
static methods receive no implicit first argument.

Callability: You can call a static method using either the class name (e.g., ClassName.method()) or an instance of the class (e.g., instance.method()).

Independence: It cannot access or modify the state of the class or its instances directly because it doesn't have access to them


Use @staticmethod when:

The logic belongs conceptually to the class but doesn't need instance or class data
It's a utility/helper function related to the class
You want to namespace a function inside a class for organization


'''    

# Example :

class validation:
    def __init__(self,username, age):
        if not validation.is_valid_gemail(username):
            raise ValueError("Invalid email") 
        
        if not validation.is_valid_age(age):
            raise ValueError("Invalid age")
        
        self.username = username
        self.age = age
    
    
    @staticmethod
    def is_valid_gemail(uname):
        return  '@' in uname and  '.' in uname 
    
    @staticmethod  
    def is_valid_age(age):
        return isinstance(age,int) and age > 0 and age < 120      
    
    

print(validation.is_valid_gemail("vijay@gmail.com"))
obj = validation("vijay@gmail.com",26)

print("Username is : ", obj.username)
print("age: ",obj.age)