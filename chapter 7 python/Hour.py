class Time:
    def __init__(self, hour = 0):
        self.setTime(hour)

    def setTime(self, hour):
        self.setHour(hour)

    def setHour(self,hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError("Invalid hour value %d" % hour)

    def getHour(self):
        return self._hour

    def printMinitary(self):
        print("%.2d" % \
              (self._hour))

    def printstandard(self):
        standardTime = ""
        if self._hour == 0 or self._hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d" %(self._hour%12)

        if self._hour < 12:
            standardTime += "AM"
        else:
            standardTime += "PM"
        print(standardTime)
