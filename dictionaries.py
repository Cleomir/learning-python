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