# Lists!
cool_students = ["Léna", "Ben", "Fabian", "Yi", "Kai", "Chris"]
print(cool_students)
# Add onto list, always last position
cool_students.append("Connor")
# Insert item anywhere in list with index
cool_students.insert(0, "Edward")
# cool_students.remove("Ryan")
print(cool_students)
# Print the last student’s name
print(cool_students[-1])
# Print up until the 4th student
print(cool_students[:3])
# Print the 2nd up until the 4th student
print(cool_students[1:3])
cool_students[1] = "Cara"
print(cool_students)
print("---")


# Dictionaries!
favorite_colors = {
    # Key     # Value
    "Fabian": "Blue", 
    "Ben":    ["Chartreuse", "Violet"], 
    "Léna":   "Puce",
    }
print(favorite_colors)
# Print Ben’s favorite color
print(favorite_colors["Ben"])
# Set Ryan’s favorite color as you add him to the dictionary
favorite_colors["Ryan"] = "Green"
print(favorite_colors)
# Print Ryan’s favorite color
print(favorite_colors["Ryan"])
print("---")


# Tuples! Like lists, but less flexible, more static.
cool_students = ("Léna", "Ben", "Fabian", "Yi", "Kai", "Chris")
print(cool_students)
# Like lists, we can get an item by its index
print(cool_students[2])
# Unlike a list, we can not assign items in tuples. They're immutable!!
# cool_students[2] = "Connor" # this raises and error

point_coordinates = (0, 20)
print(point_coordinates)
cool_color = (1,0,0)
print(cool_color)


# Sets! Like lists and tuples but each item is unique. 
# Looks like a dictionary with curly-brackets!! 
favorite_fonts = {"Neue Haas Grotesk", "Romanée", "Cancelleresca Bastarda", "Lexicon"}
print(favorite_fonts)
# Add new items with .add()
favorite_fonts.add("Beaujon")
print(favorite_fonts)
# Remove items with by their name
favorite_fonts.remove("Cancelleresca Bastarda")
print(favorite_fonts)