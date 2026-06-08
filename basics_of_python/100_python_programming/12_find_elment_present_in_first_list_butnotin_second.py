arr = [1,3,5,7,5,4]
arr2 = [4,5,6,2,1,3]

output = []

for num in arr:
    if num not in arr2:
        output.append(num)

print("output is : ",output)        