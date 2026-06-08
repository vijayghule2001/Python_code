arr = [1,3,5,7,5,4]
arr2 = [4,5,6,2,1,3]

common = []

for i in range(0, len(arr)):
    for j in range(0, len(arr2)):
        if arr[i] == arr2[j]:
            common.append(arr[i])

print("common ele in two list: ", common)            

'''
arr = [1,3,5,7,5,4]
arr2 = [4,5,6,2,1,3]

common = []

for num in arr:b
    if num in arr2:
        common.append(num)

print(common)

'''