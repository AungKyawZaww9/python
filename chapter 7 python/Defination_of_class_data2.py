from Definition import Date
class Employee:
    def __init__(self, firstName, lastName, birthMonth, birthDay,
                 birthYear, hireMonth, hireDay, hireYear):

        self.birthDate = Date(birthMonth, birthDay, birthYear)
        self.hireDate = Date(hireMonth, hireDay, hireYear)

        self.lastName = lastName
        self.firstName = firstName

        print("Employee constructor: %s, %s"\
              % (self.lastName, self.firstName))

    def __del__(self):
        print("Employee object about to be destroyed: %s, %s"\
              % (self.lastName, self.firstName))

    def display(self):
        print("%s, %s" % (self.lastName, self.firstName))
        print("Hired:", self.hireDate.display())
        print("Birthdate: ", self.birthDate.display())