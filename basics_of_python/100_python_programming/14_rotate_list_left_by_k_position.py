# 14. Write a Python program to rotate a list to the left by `k` positions.


arr = [1,2,3,4,5,6,7]
k = 2
for i in range(0,k):
    first = arr[0]
    for j in range(0,len(arr)-1):
        arr[j] =  arr[j+1]
    arr[len(arr)-1] = first

print("Rotet list left from k position: ", arr)    






