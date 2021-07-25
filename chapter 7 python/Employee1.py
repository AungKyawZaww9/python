from Employee import Employee
print("Number of employees before instantiation is", \
      Employee.count)


employee1 = Employee("Susan","Baker")
employee2 = Employee("Robert","Jones")
emplyee3 = employee1



print("Number of emplyee after instantiation is",\
      employee1.count)

del employee1
del employee2
del employee3

print("Number of emplyee after deletion is",\
      Employee.count)