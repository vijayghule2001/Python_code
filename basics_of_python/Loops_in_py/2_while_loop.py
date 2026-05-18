'''
A while loop executes a block of code as long as the condition is True.

while condition:
    # code block
    

First → condition is checked
If True → code runs
Again condition is checked
If False → loop stops
    
    
'''

# 1️⃣ Print numbers from 1 to 5

# i = 1
# num = 5 
# while  i <= num:
#     print(i)
#     i = i + 1

    
# 2 Traverse a List using while
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
i=len(numbers)
print("length: " ,i)
while i > 0 :
    print(numbers[i-1])
    i = i - 1


'''

# 5️⃣ Search Element in List (Logical Example)
'''

data = [23,43,2,45]
find = 12

found = False
i = 0
while i<len(data):
    if data[i] == find:
        found = True
        break
    i = i + 1  
if(found):
    print("Found")
else:
    print("Not Found")
    
 '''
 
#  7️⃣ Print Dictionary Keys using while

'''
 
my_dict = {"name": "Vijay", "age": 25, "city": "Pune"}
keys = list(my_dict.keys())
print(keys)

i = 0
while i < len(keys):
    print(keys[i] ," : ", my_dict[keys[i]] )
    i = i+1 



for key,value in my_dict.items():
    print("key: ", key ,"value: ", value)

'''   

 