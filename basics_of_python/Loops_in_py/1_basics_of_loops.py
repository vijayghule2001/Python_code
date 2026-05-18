'''

1.for loop : You know how many times you want to repeat.

Syntax :
    for variable in sequence:
        # code
        
2.while loop :Loop runs until condition becomes False. 
🔹 Syntax:
    while condition:
        # code

        
'''

# 1️⃣ Print Numbers from 1 to N
'''
n = int(input("Enter a number you wants : "))
for i in range(1,n + 1,1):
    print(i, end=" ")



for i in range(1,n+1):
    if i%2 == 0: 
        print(i)

# Reverse a Number (Using While Loop)

n = int(input("Enter number for reverse :"))

rev = 0
while n>0:
    digit = n%10
    rev = rev * 10 + digit
    n= n//10    
print("Reverse number: ", rev)    

# 7️⃣ Count Digits in a Number

num = int(input("Enter number for count the number : "))
count = 0

while num>0: 
    count = count +1
    num  = num // 10 

print("Number of count: ",count )    

'''
# 1️⃣ Find Sum of All Elements in a List    

nums = [3,4,5,6,8, 8]
count = 0
for num in nums:
    count = count + num 

print("Sum of all ele: ", count)    


max_ele = float('-inf') # -inf means negative infinity. 

for n in nums:
    if n > max_ele: 
        max_ele = n
        
print("Maximum ele: ", max_ele)


reverse_list =[]

for num in range(len(nums)-1,-1,-1):
    reverse_list.append(nums[num])

print("Reverse list : ", reverse_list)        


