import sys

from pip._vendor.distlib.compat import raw_input

try:
    file = open("cliente.dat","w")

except IOError:
    print(sys.stderr,"file could not be opened: ", sys.exit(3))

print("Hello")
print("Welcome to Yangon ")

while(3):
    try:
        accountline = raw_input("?")
    except EOFError:
        break
    else:
        print(file,accountline)