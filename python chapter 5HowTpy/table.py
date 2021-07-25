table1 = [ [1, 2, 3], [4, 5, 6]]
table2 = ((1,2), (3, ), (4, 5, 6))

print("\nValue in table by row are")

for row in table1:
    for item in row:
        print(item)

print("\nValue in table by row are")

for row in table2:
    for item in row:
        print(item)


