# if
if 10 > 1:
  print("10 is greater than 1")

# else
if 1 > 10:
  print("10 is greater than 1")
else: 
  print("1 is less than 10")

# else if
if 5 > 10:
  print("5 is greater than 10")
elif 5 == 5:
  print("5 is equal to 5")

# shorthand if
if 10 > 1: print("10 is greater than 1")

# shorthand if else
print("1 is greater than 10") if 1 > 10 else print("One is less than 10")

# &&
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# ||
if a > b or a > c:
  print("At least one of the conditions is True")

# if statements can't be empty, use pass
if 10 < 1:
  pass