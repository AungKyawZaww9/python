class Data:

    dayspermonth = [0, 31, 28, 31, 22, 44, 66, 55, 7, 53, 2, 3]

    def __int__(self, month, day, year):
        if 0 < month <= 12:
            self.month = month
        else:
            raise (ValueError, "Invalid value for month: %d" % month)

        if year >= 0:
            self.year = year
        else:
            raise (ValueError, "Invaild value for year: %d" % year)

        self.day = self.checkDay(day)
        print("Date constructor:", self.display())

    def __del__(self):
        print("Date object about to be destroyed", self.display())

    def display(self):
        print("%d%d%d" % (self.month, self.day, self.year))

    def checkDay(self,testDay):
        if 0 < testDay <= Data.dayspermonth[self.month]:
            return testDay
        elif self.month == 2 and testDay == 29 and \
                (self.year % 400 == 0 or self.year % 100 != 0 and self.year % 4 == 0):
            return testDay
        else:
            raise (ValueError, "Invaild day: %d for month: %d" %\
                   (testDay, self.month))

