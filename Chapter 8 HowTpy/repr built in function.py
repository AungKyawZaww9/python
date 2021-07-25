class Person:
    name = 'Admin'
    def __repr__(self):
        return repr('Hello ' + self.name)

print(repr(Person()))