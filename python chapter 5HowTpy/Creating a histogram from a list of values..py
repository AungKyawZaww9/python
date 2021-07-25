from pip._vendor.distlib.compat import raw_input

values = []

print("Enter 10 values:")


for i in range(10):
    newvalue = int( raw_input("Enter integer %d: " % (i+1)))
    values += [newvalue]

print("\nCreating a historgram from values: ")
print("%s %10s %10s" % ("Element", "Value","Historgam" ))

for i in range(len(values)):
    print( "%7d %10d %11s" % (i, values[i], "=" * values[i]))

