
# [1, 3, 5, 6, 0, 0, 0]

arr = [1, 3, 0, 5, 0, 6, 0]
j = 0
for i in range(len(arr)):
    if arr[i] != 0 :
        temp = arr[i]
        arr[i] =  arr[j]
        arr[j] = temp
        
        j += 1
        
print(arr)