# basic declaration
x = 5
y = "John"

print(x)
print(y)

# assign types
x = str(3)
y = int(3)
z = float(3)

print(type(x))
print(type(y))
print(type(z))

# case-sensitive
X = "Python is case-sensitive"

print(x)
print(X)

# variable names
#$invalidVariable = "Not allowed"

_allowed = "true"

print(_allowed)

# arrays
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits

print(fruits)
print(x)
print(y)
print(z)

print(x + " is a fruit")

def myFunc():
  global x
  x = "fantastic"

myFunc()
print("Python is " + x)
