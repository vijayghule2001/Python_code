# 16. Write a Python program to find the frequency of each element in a list.

arr = [1,2,3,4,5,2,1,3,4,1,2,4]
freq= {}

for  num in arr:
    freq[num] = freq.get(num,0)+1

print("Frequency of ele: ", freq)    