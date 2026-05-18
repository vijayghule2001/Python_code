arr = [1, 2, 3, 2, 4, 1, 5,5]

large = float('-inf')
sec_large =  float('-inf')

for  num in arr:
    if num > large:
        sec_large =  large
        large =  num
    elif num > sec_large  and  num != large:
        sec_large = num 

print("Large Ele in list: ", large)
print("Second large ele in list : ", sec_large)        