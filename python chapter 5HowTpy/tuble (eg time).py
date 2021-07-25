from pip._vendor.distlib.compat import raw_input


hour = int(raw_input("Enter hour: "))
minute = int(raw_input("Enter minute: "))
second = int(raw_input("Enter second: "))

currenttime = hour, minute, second

print("The value of current time: ", currenttime)

print("The number's second :",\
      (currenttime[0] * 3600 + currenttime[1] * 60 + currenttime[2]))