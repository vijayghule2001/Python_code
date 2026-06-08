# 15. Write a Python program to rotate a list to the right by `k` positions.

arr = [1,2,3,4,5,6,7]
k = 2

for i in range(0,k):
    last = arr[len(arr)-1]
    print(last)
    for j in range(len(arr)-2,-1,-1):
        arr[j+1] = arr[j]
    
    arr[0] = last   
     
print(arr)    