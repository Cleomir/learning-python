# inheritance without overriding
class Parent:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName

  def printName(self):
    print(self.firstName, self.lastName)

class Child(Parent):
  pass

child = Child("John", "Jr.")
child.printName()

# inheritance with overriding
class ChildWithOverride(Parent):
  def __init__(self, firstName, lastName):
    Parent.__init__(self, firstName, lastName)

# super
class ChildWithSuper(Parent):
  def __init__(self, firstName, lastName):
    super().__init__(firstName, lastName)

# add properties and methods in child
class ChildPropertiesAndMethods(Parent):
  def __init__(self, firstName, lastName, year):
    super().__init__(firstName, lastName)
    self.graduationYear = year

  def printDetails(self):
    print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)

student = ChildPropertiesAndMethods("Mike", "Olsen", 2021)
student.printDetails()