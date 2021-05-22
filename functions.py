# declaration
def simpleFunction():
  print("Hello from simpleFunction")

# invocation
simpleFunction()


# with arguments
def functionWithArguments(firstName):
  print(firstName + " Doe")
functionWithArguments("John")

# rest operator
def restOperatorFunction(*kids):
  print("The youngest child is " + kids[2])
restOperatorFunction("Emil", "Tobias", "Linus")

# kwargs
def kwargsFunction(**kid):
  print("His last name is " + kid["lastName"])
kwargsFunction(firstName = "Tobias", lastName = "Doe")

# default parameter
def functionWithDefaultParameter(country = "Ukraine"):
  print("The country selected is " + country)
functionWithDefaultParameter()

# return values
def functionWithReturnValues(number):
  return 2 * number
functionWithReturnValues(2)

# empty functions
def emptyFunction():
  pass