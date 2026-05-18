class Student:
    students = []
    
    
    def __init__(self,name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age
        studentData = self.createAnDict()
        Student.students.append(studentData)
        
    def createAnDict(self):
        obj = {
            "name" : self.name,
            "marks" : self.marks,
            "age" : self.age
        }  
        return obj
    
    
    def showStudentDetails(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Age: {self.age}")


s1 = Student("vijay", 89.20, 26)
s1.showStudentDetails()  
print(Student.students)     

s2 =  Student("amol", 78, 23)
s2.showStudentDetails()
print(Student.students)    