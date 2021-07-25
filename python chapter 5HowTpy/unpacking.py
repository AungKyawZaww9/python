astring = "abc"
alist = [1,2,3]
atuple = "a", "A", 1

print("Unpacking string :")
first, second , third = astring

print("String value: ", first, second , third)

print("Unpacking list :")
first, second, third = alist

print("String list: ", first, second, third)

print("Unpacking tuple..")
first, second, third = atuple
print("tuple : ", first, second , third)

x = 3
y = 4

print("\nBefore swap: x = %d , y = %d" % (x, y))
x ,y = y,x #swapping
print("\nAfter swap: x = %d , y = %d" % (x, y))



