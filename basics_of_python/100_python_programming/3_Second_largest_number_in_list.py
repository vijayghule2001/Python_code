li = [2,4,6,1,7,8,4]
largest = float('-inf')
sec_large = float('-inf')

for num in li:
    if num > largest:
        sec_large = largest
        largest =  num
    elif  num > sec_large and num < largest:
        sec_large = num 


print("Second larges number in list : ", sec_large)            