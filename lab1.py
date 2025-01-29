arr = [10,89,9,56,4,80,8]

max= arr[0]
min= arr[0]
for num in arr:
    if num > max:
        max= num
    if num < min:
        min = num
print(f"Largest element: {max}")
print(f"Smallest element:{min}")
