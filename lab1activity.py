arr = [10,89,9,56,4,80,8]
arr = list(set(arr))
arr.sort()
second_smallest = arr[1]
second_largest = arr[-2]
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)
