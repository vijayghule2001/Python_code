li = [1,2,30,40,2,4]
large = float('-inf')

for num in li:
    if num > large:
        large = num

print("Largest number in list: ", large)        