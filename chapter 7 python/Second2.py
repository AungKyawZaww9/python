from Second1 import Time

time1 = Time()

print("The initial military time is :",time1.printMilitary())

print("\nThe initial standard time is :",time1.printstandard())


time1.setTime( 7, 37, 40)
print("\n\nMilitary time after setime is :", time1.printMilitary())

print("\nStandard time after settime is :", time1.printstandard())

time1.setHour(4)
time1.setMinute(3)
time1.setSecond(6)
print("\nMilitary time after Set.Hour,Minute,Second :",time1.printMilitary())
print("\n\nStandard tme after :", time1.printMilitary())