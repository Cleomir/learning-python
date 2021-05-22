# declaration
class SimpleClass:
  name = "John Doe"

# instantiation
simpleObject = SimpleClass()
print(simpleObject.name)

# constructor
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person = Person("John", 36)
print(person.name)
print(person.age)

# object methods
class PersonWithMethods:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printName(self):
    response = "Hello my name is {0} and I am {1}"
    print(response.format(self.name, self.age))

personWithMethods = PersonWithMethods("John", 36)
personWithMethods.printName()

# delete property
del personWithMethods.age