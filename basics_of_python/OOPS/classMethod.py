class Car:
    carProduction = "TATA"
    
    def __init__(self,carName):
        self.carName = carName
    
    @classmethod
    def getProduction(cls):
         return f"My car Production is : {cls.carProduction}"


obj = Car("swift")

production = obj.getProduction()
print(obj.carName)
print(production)     
     