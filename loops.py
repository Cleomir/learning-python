# while
i = 1
while i < 6:
  print(i)
  i += 1

# break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue
i = 1
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# else 
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# for
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# looping through a string
for letter in "apple":
  print(letter)

# range(starts in 0)
for i in range(6):
  print(i)

# else
for i in range(6):
  print(i)
else:
  print("the loop has ended")

# loops can't be empty, use pass
for number in [0, 1, 2]:
  pass