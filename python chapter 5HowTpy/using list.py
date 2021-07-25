alist = []

for number in range(1,11):
    alist += [number]

print("The value of alist is: ", alist)

print("\nAccessing values by iteration: ")

for item in alist:
    print(item)


print("\nAccessing values by index: ")
print("Subscript        value")

for i in range(len(alist)):
    print("%9d %7d " % (i, alist[i]))

print("\nModifying a list value :")
print("Value of alist before modification: ", alist)

#alist[0] = -100
alist[-3] = 19

print("value of alist after modification : ", alist) # if - from buttom to upper

