
from time import Time

time1 = Time()

print('The attributes of time1 are:')
print("time1.hour:",time1.hour)
print("time1.min : ",time1.minute)

print("\nCalling printmilitary :",time1.printmilitary())


print("\ncalling standard : ",time1.printstandard())


print("\nChanging time number")
time1.hour = 25
print("calling ....",time1.printmilitary())

