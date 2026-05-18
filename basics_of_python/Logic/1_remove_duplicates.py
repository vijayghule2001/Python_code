
# Solution :01

# arr = [1, 2, 3, 2, 4, 1, 5]
# result = []

# for i in range(0, len(arr)):
#     found = False
#     for j in range(0,len(result)):
#         if arr[i] == arr[j]:
#            found  = True
#            break
#     if not found:
#         result.append(arr[i])     
# print("Remove dup:", result)            




# Solution :02

arr = [1, 2, 3, 2, 4, 1, 5]
result = []

for i in range(0, len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
print("Remove Duplicates: ", result)        
        
