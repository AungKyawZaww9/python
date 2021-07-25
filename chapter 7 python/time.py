class Time:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def printmilitary(self):
        print("\t\t%.2d:%.2d:%.2d"%\
               (self.hour, self.minute, self.second))

    def printstandard(self):
        standardtime = ""

        if self.hour == 0 or self.hour == 12:
            standardtime += "12:"
        else:
            standardtime += "%d:" % (self.hour % 12)
        standardtime += "%.2d:%.2d" % (self.minute, self.second)

        if self.hour < 12:
            standardtime += "AM"

        else:
            standardtime += "PM"

        print(standardtime)

