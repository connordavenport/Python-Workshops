# Store a string in a variable
my_string = "first string"
# Redefine the variable with a different string
my_string = "other string"
# Add an emoji to the end of the string
my_string += "🐍"
# Multiply the string * 100
my_string *= 100

# Print the string
print(my_string)

# Reset the string
my_string = "second string " * 10
# Custom string formatting with variables
# A string with the f prefix is an f-string
# This is a special string object that can
# store variables inside of curly braces
print(f"my string is: {my_string}")
# You can also use functions inside an f-string
print(f"my range is: {list(range(10))}")
# And more complex nested functions 
print(f"my numbers are: {' '.join([str(i) for i in list(range(10))])}")