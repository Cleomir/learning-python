fruits = ["apple", "banana", "cherry"]
print(fruits)

# length
print(len(fruits))

# arrays are objects of the class list
print(type(fruits))

# arrays can be created via a constructor
fruits = list(("apple", "banana", "cherry"))
print(fruits)

# accessing items
print(fruits[1])

# accessing items from the end
print(fruits[-1])

# slice
print(fruits[1:3])

# slice (up to index)
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[:3])

# slice (from index)
print(fruits[3:])

# slice (negative range)
print(fruits[-4:-1])

# includes
if "mango" in fruits:
  print("Mango is in the fruits array")