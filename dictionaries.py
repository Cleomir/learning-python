basicDictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(basicDictionary)

# length
print(len(basicDictionary))

# type
print(type(basicDictionary))

# accessing property
print(basicDictionary["brand"])
print(basicDictionary.get("brand"))

# keys
dictionaryKeys = basicDictionary.keys()
print(basicDictionary.keys())
basicDictionary["color"] = "white"
print(basicDictionary.keys())

# values
print(basicDictionary.values())

# element
print(basicDictionary.items())

# check if exists
if "model" in basicDictionary:
  print("model is in basic dictionary")

# change property
basicDictionary["year"] = 2021
print(basicDictionary)
basicDictionary.update({"year": 2020})
print(basicDictionary)

# add property
basicDictionary["doors"] = 4
print(basicDictionary)

# delete property
del basicDictionary["doors"]
print(basicDictionary)

# loop through keys
for key in basicDictionary:
  print(key)

# loop through values
for key in basicDictionary:
  print(basicDictionary[key])

# copy
copiedDictionary = basicDictionary.copy()
print(copiedDictionary)

# nested dictionary
nestedDictionary = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  }
}
print(nestedDictionary)

# clear
basicDictionary.clear()
print(basicDictionary)

