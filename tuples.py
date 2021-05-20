# one item tuple
fruitTuple = ("apple",)
print(type(fruitTuple))

# not a tuple
fruitTuple = ("apple")
print(type(fruitTuple))

# tuple constructor
fruitsTuple = tuple(("apple", "banana", "cherry"))
print(fruitsTuple)
print(type(fruitsTuple))

# accessing tuple items
print(fruitsTuple[0])

# accessing tuple items from the end
print(fruitsTuple[-1])

# accessing a range
print(fruitsTuple[1:2])

# includes
if "cherry" in fruitsTuple:
  print("Cherry is in the tuple")

# destructuring
(apple, banana, cherry) = fruitsTuple
print(apple, banana, cherry)

# destructuring into an array
(apple, *banana) = fruitsTuple
print(apple, banana)

# for
for fruit in fruitsTuple:
  print(fruit)

# for with indexes
for i in range(len(fruitsTuple)):
  print(fruitsTuple[i])

# while
i = 0
while i < len(fruitsTuple):
  print(fruitsTuple[i])
  i += 1

# join
numberTuple = (1, 2, 3)
joinedTuple = numberTuple + fruitsTuple
print(joinedTuple)

# multiply the content 
doubleFruitsTuple = fruitsTuple * 2
print(doubleFruitsTuple)