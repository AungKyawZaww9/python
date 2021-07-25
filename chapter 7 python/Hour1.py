from Hour import Time
def printTimeValues(timetoprint):
    timetoprint.printMilitary()

    timetoprint.printstandard()

time1 = Time()
time2 = Time(2)
time3 = Time(21)
time4 = Time(12)

print("\nall arguments defaulted: ")
print(printTimeValues(time1))

print(printTimeValues(time2))
