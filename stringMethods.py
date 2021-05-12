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

# slice
b = "Hello, World!"
print(b[2:5])

# slice from start
print(b[:5])

# slice to the end
print(b[2:])

# slice from the end
print(b[-5: -2])

# uppercase
print(b.upper())

# lowercase
print(b.lower())

# trim
c = "    Hello, World!    "
print(c.strip())

# replace
print(b.replace("H", "J"))

# split
print(b.split(","))