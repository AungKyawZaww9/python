
#Getattar
class Person:
    age = 23
    name = "Adam"
    qualification = "MA"
person = Person()
print('The age is:', getattr(person, "qualification"))
print('The age is:', person.name)

#Setattar
class Person:
    name = 'Adam'
    age = 45

p = Person()
print('Before modification:', p.name, p.age)

# setting name to 'John'
setattr(p, 'name', 'John' )
setattr(p,'age',33)

print('After modification:', p.name, p.age)

