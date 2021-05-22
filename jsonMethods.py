import json

# parse
stringifiedJSON = '{ "name":"John", "age":30, "city":"New York"}'
parsedJSON = json.loads(stringifiedJSON)
print(parsedJSON)

# stringify
object = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
stringifiedObject = json.dumps(object, indent=2)
print(stringifiedObject)