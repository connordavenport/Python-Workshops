import time

# Everything in python is an object, this allows us to
# give anything special abilites under the hood


# String dunders

# __abs__(self):
# returns absolute value of value
print(abs(-100))

# __neg__(self):
#  returns negative value of value
x = 100
print(-x)
# >> -100 

# __pos__(self):
#  returns positive value of value
x = -100
print(+x)
# >> 100 

# __add__(self, other):
#  returns sum of two values, any object can subclass this 
# inheret the function
print(1 + 2)
print("a" + "b")
# >> 3
# >> ab
# custom implementation:
# def __add__(self, other):
#   return chr(ord(str(self)) + ord(str(other)))
# >> Ã

# __sub__(self, other):
#  returns subtraction of two values, any object can subclass this
print(2 - 1)

# __mul__(self, other):
#  returns multiplication of two values

# __str__(self):
#  returns string of object
a = 100
print(str(a))
# >> "100"

# __repr__(self):
# returns represetnation of object
class a():
    def __repr__(self):
        return f"<connors_object@{time.time()}>"
x = a()
print(x)

# __bool__(self):
# returns boolean of object
class b():
    def __init__(self, number):
        self.number = number
    def __bool__(self): # You can make this do whatever you want
        return True if self.number % 2 == 0 else False
c = b(3)
print(bool(c))

# __eq__(self, other):
# returns boolean of object against another object
print(1 == 2)

# __ne__(self, other):
# returns boolean of object against another object
print(1 != 2)

# __lt__(self, other):
# returns boolean of object against another object
print(1 < 2)

# __gt__(self, other):
# returns boolean of object against another object
print(1 > 2)

# __ge__(self, other):
# returns boolean of object against another object
print(1 >= 2)

# __le__(self, other):
# returns boolean of object against another object
print(1 <= 2)


# Put it all together
class Bicycle():
    

    def __init__(self):
        self.name = ""
        self.speed = 100 # rpm
        

    # Python has a ton of built in "dunder methods" to add special
    # functions to your objects
    def __repr__(self):
        return f"<{self.name}'s Bicycle @ {self.speed} RPM>"

    # doing complex things *outside* the class
    def __eq__(self, other):
        return (self.speed == other.speed) and (self.name == other.name)
        
    def __ne__(self, other):
        return (self.speed != other.speed) and (self.name != other.name)
        
    def __lt__(self, other):
        return self.speed < other.speed
        
    def __gt__(self, other):
        return self.speed > other.speed
        
    def __ge__(self, other):
        return self.speed >= other.speed

    def __le__(self, other):
        return self.speed <= other.speed
        


    def ride(self):
        rotations = 4 # arbitrary amount of rotations
        for i in range(rotations):
            time.sleep(60/self.speed)
            #print(f"{i} rotations")
        print(f"🏁 {self.name} finished riding")


    def race(self, other_bike):
        # good for internal usage
        result = "Won"
        if self.speed < other_bike.speed:
            result = "Lost"
        elif self.speed == other_bike.speed:
            result = "Tied"
        return f"{self.name} {result}"


# # Establish two bicycles, set their names, and make them ride
tadej = Bicycle()
tadej.name = "Tadej"

jonas = Bicycle()
jonas.name = "Jonas"

tadej.speed = 130
jonas.speed = 120
#tadej.ride()
#jonas.ride()

print(tadej)

print(tadej > jonas)
print(tadej < jonas)
print(tadej == jonas)
#print(tadej.race(jonas))

