"""
In Python, keyword arguments are arguments that are preceded by an identifier (the parameter’s name) when you call a function.
They make your code easier to read and allow you to change the order of arguments when calling a function.
"""
def hello(greeting, title, first, last):
    print(greeting, title, first, last)

# Call the function with positional arguments - this means the order matters:
hello("Hello", "Mr.", "Evan", "Burlingame")
# What happens when we change the order?:
hello("Evan", "Hello", "Burlingame", "Mr.")
# Try again with keyword arguements:
hello(first = "Evan", greeting = "Hello", last = "Burlingame", title = "Mr.")

# Note: You can mix, but potisional args must be first:
hello("Hello", "Mr.", last = "Burlingame", first = "Evan")