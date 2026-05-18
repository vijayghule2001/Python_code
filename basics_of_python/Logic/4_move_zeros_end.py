# Move all zeros to end
"""
arr = [0, 1, 0, 3, 12]
result = []

for i in range(0,len(arr)):
    if arr[i] != 0:
        result.append(arr[i])

for i in range(0,len(arr)):
    if arr[i] == 0 :
        result.append(arr[i])       

print("Move all zero end of the list: ", result)        

"""
arr = [1, 0, 2, 0, 4, 0, 5]

result = []

def move_zero(index):
    
    if index == len(arr):
        return
    
    if arr[index] != 0:
        result.append(arr[index])

    move_zero(index + 1)

    if arr[index] == 0:
        result.append(arr[index])

move_zero(0)
print("Using recursion: ", result)    
        
        
'''
What is Recursion?
A function calling itself again and again until some condition stops it.        








'''