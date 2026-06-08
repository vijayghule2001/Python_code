numbers = [10, 20, 30, 40, 50,2,3,5,2,]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    
    else:
        odd.append(num)    

print("Even numbers in list:", even)
print("odd numbers in list:", odd)