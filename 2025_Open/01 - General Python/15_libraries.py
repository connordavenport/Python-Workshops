# Into on using libraries inside scripts

# Python has a lot of default libraries built in that we can utilize
# os is Python's library to access "operating system" commands
import os

# Get the current working directory
print(os.getcwd())
# Split a path into a directory and file basename
print(os.path.split("~/path/to/my/font.ufo"))
# Get the absolute path of a filename
print(os.path.abspath("10-functions.py"))
# Check if a file exists on your machine
print(os.path.exists("/System/Library/Fonts/SFNS.ttf"))


# sys is "System-specific" parameters and functions
import sys
# We can print out all default libraries that are packaged in Python
print(sys.stdlib_module_names)

# We can also pick and choose what we import instead of an entire library
from math import cos, sin, degrees, radians
# Convert radians angle to degrees
degree = 45
radian = round(radians(degree), 3)
# Print output in an f-string
print(f"angle {degree}˚ is equal to {radian}㎭ in radians")
radian = .666
# Round converted degree to 3 decimels
degree = round(degrees(radian), 3)
print(f"angle {radian}㎭ is equal to {degree}˚ in degree")

# Import a time library
import time
# Log the starting time as a variable
start = time.time()
# Loop over a very large range iterator
for i in range(100000000):
	# dont actually do anything for now
	pass
# Log the end time as a variable
end = time.time()
# Subtract the start time from end time
print(f"It took us {round(end-start, 3)} seconds to run this function")