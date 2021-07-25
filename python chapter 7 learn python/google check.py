'''import keyword

# initializing strings for testing while putting them in an array
keys = ["for", "while", "tanisha", "break", "sky",
        "elif", "assert", "pulkit", "lambda", "else", "sakshar"]

for i in range(len(keys)):
    # checking which are keywords
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not a python keyword")'''

'''a = 5

print(type(a))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))'''

'''my_list = ['p', 'r', 'o', 'b', 'e']

# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][4])

print(n_list[1][3])

# Error! Only integer can be used for indexing
print(my_list[4.0])



odd = [1, 3, 5]

odd.append(8)

print(odd)

odd.extend([9, 11, 13])

print(odd)

print(["re"] * 4)

del odd[2]

print(odd)

del odd[1:5] # 1 and 5 not inclued , another include

print(odd)

my_tuple = ("hello")
print(my_tuple)
print(type(my_tuple))

my = ()
print(type(my))
print("\n\n\n")

my_tuple = (4, 2, 3, [6, 5])

my_tuple[3][1] = 9   
print(my_tuple)


str = 'programiz'
print('str = ', str)


print('str[0] = ', str[0])


print('str[-1] = ', str[-1])


print('str[1:5] = ', str[0:10])


print('str[5:-2] = ', str[5:-2])'''

print("\n")
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

print("\n")
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

print(my_set)