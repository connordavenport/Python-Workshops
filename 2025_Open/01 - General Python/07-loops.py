# LOOPS!!

objects_on_my_desk = ["glass", "headphones", "keyboard", "mouse"]

# Loop through each object
for object_on_desk in objects_on_my_desk:
    # and each time do this..,
    print(0)
    print(1)
    print(3)
    # and if the object’s name is longer than 6 letters,...
    if len(object_on_desk) > 6:
        # do this
        print(object_on_desk)
    # Print a line break
    print()
    
    
# Looping over a range
# range() creates an object that allows you to 
# iterate over between two numbers

# go from 0-20
# If you want it to end with 20, you need to add 
# the increment to the stop value, e.g. (0,21)
our_range = range(21)
print(our_range)
print(list(our_range))

for i in our_range:
    print(i)

# Range takes 3 arguments, start, stop, and step
# start, optional 
# end, required
# step, optional
# the last is the increment, 1 is the default
another_range = range(0, 25, 5)
print(another_range)
print(list(another_range))

for i in another_range:
    print(i)