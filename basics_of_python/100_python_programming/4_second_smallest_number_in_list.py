li = [2,4,6,1,7,8,4]

smallest = float('inf')
sec_smallest = float('inf')

for num in li:
    if num < smallest:
        sec_smallest = smallest
        smallest = num
    elif num > smallest and num < sec_smallest:
        sec_smallest = num

print("Smallest:", smallest)
print("Second Smallest:", sec_smallest)
  