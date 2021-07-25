class Employee:
    count = 0

    def __int__(self, first, last):
        self.firstName = first
        self.lastName = last


        Employee.count += 1
        print("Employee constructor for %s, %s" \
             % (self.lastName, self.firstName))

    def __del__(self):
        Employee.count -= 1

        print("Employee destructor for %s , %s" \
              % (self.lastName, self.firstName))


R1 = Employee()
print(R1.firstName)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John u", 36)

print(p1.name)
print(p1.age)

