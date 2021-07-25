def modifyllist(alist):

    for i in range(len(alist)):
        alist[i] *= 2

def modifyelement(element):
    element *= 2

alist = [1, 2, 3, 4, 5]

print("Effect of passing entire list")
print("The value of the original list are: ")

for item in alist:
    print(item)

modifyllist(alist)
print("\nThe value of the modify list are: ")

for item in alist:
    print(item)

print("\nEffect of passing element ")
print("alist[3] before modifyelement: ",alist[3])

modifyelement(alist[3])
print("Modify element ",alist[3])

print("\nEffect of passing element ")
print("alist[3] before modifyelement: ",alist[2:4])

modifyelement(alist[1:5])
print("Modify element ",alist[1:5])