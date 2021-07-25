class Time:
    def __init__(self):
        self._hour =0
        self._minute = 0
        self._second = 0

    def setTime(self, hour, minute, second):
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def setHour(self, hour):
        if hour >= 0 and hour < 24:
            self.hour = hour
        else:
            raise ValueError("Invaid hourvalue : %d") % hour

    def setMinute(self, minute):
        if 0 <= minute < 24:
            self._minute = minute
        else:
            raise ValueError("Invaid hourvalue : %d") % minute

    def setSecond(self, second):
        if 0 <= second < 24:
            self._second = second
        else:
            raise ValueError("Invaid hourvalue : %d") % second

    def getHour(self):
        return self._hour

    def getMinute(self):
        return self._minute

    def getSecond(self):
        return self._second

    def printMilitary(self):
        print("%.2d:%.2d:%.2d") % \
        (self._hour, self._minute, self._second),

    def printstandard(self):
        standardTime = ""
        if self._hour == 0 or self.hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % (self._hour % 12)

        standardTime += "%.2d:%.2d" % (self._minute, self._second)

        if self.hour < 12:
            standardTime += "AM"
        else:
            standardTime += "PM"
        print(standardTime)