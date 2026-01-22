# What exactly is a boolean?
# yes/no true/false 0/1
# In python we can have different types of objects
# that act as a boolean so its important to pay attention to 
# your data types!!

my_value = 0

if my_value:
	print("its there")
else:
	print("hey wheres my values?!")

# Even though we have a value set, python treats zero as False
print(my_value == False)
# If we make it check against None, we get an accurate output
if my_value is not None:
	print("its there:)")

print(0 == False)
print(0 == [])
print(0 == None)

print(1 == True)
print(1 == ["1"])
print(1 == None)

# Not all returned values are the same

# Even though an empty list, 0, and False are all acting
# in the same way below, they are not equal to each other!
my_list = []
if my_list:
	print("my list is here")
else:
	print("my list is missing")
my_list.append("item")
if my_list:
	print("my list is here")
else:
	print("my list is missing")