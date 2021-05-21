# simple set
fruitsSet = {"apple", "banana", "cherry"}
print(fruitsSet)

# length
print(len(fruitsSet))

# type
print(type(fruitsSet))

# set constructor
fruitsSet = set(("apple", "banana", "cherry"))
print(fruitsSet)

# for
for fruit in fruitsSet:
  print(fruit)

# check if item is in set
print("banana" in fruitsSet)

# add item
fruitsSet.add("orange")
print(fruitsSet)

# merge set
tropicalFruitsSet = {"pineapple", "mango", "papaya"}
fruitsSet.update(tropicalFruitsSet)
print(fruitsSet)

# delete item
fruitsSet.discard("papaya")
print(fruitsSet)

# clear
tropicalFruitsSet.clear()
print(tropicalFruitsSet)

# delete set
# del tropicalFruitsSet

# join sets
numbersSet = {1, 2, 3}
joinedSet = fruitsSet.union(numbersSet)
print(joinedSet)

# keep only duplicates
variedSet = {"google", "microsoft", "apple"}
set3 = fruitsSet.intersection(variedSet)
print(set3)

# keep all, but not duplicates

set4 = fruitsSet.symmetric_difference(variedSet)
print(set4)