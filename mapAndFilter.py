#Using map and filter function with lambda
numbers = [15, -3, 42, -7, 8, 100, -1, 55, 23, -9]

positives = list(filter(lambda x: x > 0, numbers))

below_50 = list(filter(lambda x: x < 50, positives))

doubled = list(map(lambda x: x * 2, below_50))

evenNumbers = list(filter(lambda x: x % 2 == 0, doubled))

sorts = sorted(evenNumbers)

print(f"Original list: {numbers}")
print(f"After removing negatives: {positives}")
print(f"After keeping below 50: {below_50}")
print(f"After doubling: {doubled}")
print(f"After keeping only even numbers: {evenNumbers}")
print(f"Sorted Even Numbers: {sorts}")