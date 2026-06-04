li = [1,2,3,4,5,8,3,0,-5]
smallest = float('inf')

for num in li:
    if num < smallest:
        smallest = num

print("Smallest number in list: ", smallest)        