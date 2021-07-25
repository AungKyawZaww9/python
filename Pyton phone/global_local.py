x = 10


def num():
    x = 20
    x += 1
    print(x)


def num1():
    global x
    x += 2
    print(x)


print(x)
num()
num1()






