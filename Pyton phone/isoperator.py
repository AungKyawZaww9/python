minum = None  # None is built-in

for i in [10002, 23, 23, 3466, 45, 6, 5640000]:
    if minum is None:  # is not operator also has
        minum = i
    elif i < minum:
        minum = i

    print("current number", i, "minum", minum)

print("Min is ", minum)
