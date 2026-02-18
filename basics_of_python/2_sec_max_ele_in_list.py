List = [1,12,6,12,6]

max_ele = float('-inf') # -inf means negative infinity. 
sec_max = float('-inf')

for num in List:
    if num > max_ele:
        sec_max = max_ele
        max_ele = num
        
    elif num < max_ele and num > sec_max:
        sec_max = num

print("Max element : ", max_ele)        
print(" Second Max element : ", sec_max)

# Notes
# float('inf') = positive infinity
# It is greater than any number