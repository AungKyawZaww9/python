alist = [ 1, 2, 4, 5, 8, 99, 66, 44, 0]

print("Data item in original order")

for item in alist:
    print(item)

alist.sort()

print("\nData item in after sorting order")

for item in alist:
    print(item)