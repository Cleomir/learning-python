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

# replace adding items in array
fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)

# replace removing items in array
fruits[1:3] = ["watermelon"]
print(fruits)

# add item to a specific position
fruits.insert(1, "pineapple")
print(fruits)

# push
fruits.append("strawberry")
print(fruits)

# add array at the end
moreFruits = ["papaya"]
fruits.extend(moreFruits)
print(fruits)

# splice
fruits.remove("apple")
print(fruits)

# remove specific index
fruits.pop(3)
print(fruits)

# pop
fruits.pop()
print(fruits)

# delete array
# del fruits

# clear array
# fruits.clear()
# print(fruits)

# loop through array
for fruit in fruits:
  print(fruit)

# loop through array via indexes
for i in range(len(fruits)):
  print(fruits[i])

# looping via while
i = 0
while i < len(fruits):
  print(fruits[i])
  i += 1
