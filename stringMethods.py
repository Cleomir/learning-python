# multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# strings are arrays
a = "Hello, World!"
print(a[0])

for x in a:
  print(x)

# string length
print(len(a))

# check if string includes a string
text = "The best things in life are free!"
print("free" in text)

# check if string doesn't include a string
text = "The best things in life are free!"
print("expensive" not in text)