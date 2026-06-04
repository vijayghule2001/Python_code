arr = [1,2,6,4,3,2,7,6,4,3]
# unique = [] 
# for num in arr:
#     if num not in unique:
#         unique.append(num)

# print("Remove Dup Ele: ", unique)        

for i in range(0,len(arr)):
    for j in range(i+1, len(arr)-1):
        if arr[i] == arr[j]:
            arr.pop(j)
            
print(arr)            