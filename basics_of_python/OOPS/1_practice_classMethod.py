class Student: 
    def __init__(self,name, **kwargs):
        self.name = name 
        self.marks = kwargs

    def findAverage(self):
        total = 0
        for key, val in self.marks.items():   # ✅ .items() gives key-value pairs
            total = total + val

        avg = total / len(self.marks)         # ✅ divide by number of subjects

        print(f"Student  : {self.name}")
        print(f"Marks    : {self.marks}")
        print(f"Total    : {total}")
        print(f"Average  : {avg:.2f}")        # :.2f
        
s1  =  Student("vijay", marathi = 25, english = 34)
s1.findAverage()
                