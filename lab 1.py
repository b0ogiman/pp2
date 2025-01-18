print("Hello, World!")

if 5 > 2:
  print("Five is greater than two!")

  if 5 > 2:
        print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

x = 5
y = "Hello, World!"

#This is a comment.

"""
This is a comment
written in
more than just one line
"""
x = 5
y = "John"
print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

for x in "banana":
  print(x)


txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


b = "Hello, World!"
print(b[2:5])