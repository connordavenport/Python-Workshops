# Make a function that OUTPUTS "hi" a given amount of times in a given language
def give_greeting(how_many_times=1, language="en"):
     if language == "es":
          greeting = "hola"
     elif language == "ar":
          greeting = "مرحبًا"
     elif language == "zho":
          greeting = "你好"
     elif language == "iri":
          greeting = "dia dhuit"
     else:
          greeting = "hi"

     return f"{greeting} " * how_many_times

# Store the output of the function (given input 200)
my_greeting = give_greeting(10, "ar")

# Print the output
print(my_greeting)



# Arguments without a defined set of required names
def give_greeting(**kwargs):

     # Kwargs is a dictionary of arguments and their keywords

     language = kwargs.get("language", "en")
     amount = kwargs.get("how_many_times", 1)

     if language == "es":
          greeting = "hola"
     elif language == "ar":
          greeting = "مرحبًا"
     elif language == "zho":
          greeting = "你好"
     elif language == "iri":
          greeting = "dia dhuit"
     else:
          greeting = "hi"

     return f"{greeting} " * amount

# Store the output of the function (given input 200)
my_greeting = give_greeting(how_many_times=3, language="es")
# Print the output
print(my_greeting)

# Since dictionaries can use .get() we can also store a fallback
# so if no arguments are passed it will default to 'english' and 1

my_greeting = give_greeting()
print(my_greeting)


# We can also add both args and kwargs to make flexible functions
def give_greeting(*args, **kwargs):

     # Args is a tuple of raw arguments with no predefined names
     output = ""
     language = kwargs.get("language", "en")
     amount = kwargs.get("how_many_times", 1)

     if language == "es":
          greeting = "hola"
     elif language == "ar":
          greeting = "مرحبًا"
     elif language == "zho":
          greeting = "你好"
     elif language == "iri":
          greeting = "dia dhuit"
     else:
          greeting = "hi"

     for name in args:
          output += f"{greeting} {name}, " * amount
          output += "\n" # add line break after each name entry

     return output

# In this case we can give the function any number of names to greet
my_greeting = give_greeting("connor", "ryan", "ben", "nick", how_many_times=3, language="es")
# Print the output
print(my_greeting)






