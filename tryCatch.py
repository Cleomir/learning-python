# syntax
try:
  print(x)
except:
  print("An exception occurred")

# else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The try except is finished")

# throw exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")