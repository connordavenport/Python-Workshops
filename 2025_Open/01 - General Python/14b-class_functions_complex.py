import time



# Make an object template for Bicycle
class Bicycle():
    
    # ... that starts with an empty name attribute
    def __init__(self):
        self.name = ""
        self.speed = 100 # rpm
        
    # ... and has a function for riding
    def ride(self):
        rotations = 4 # arbitrary amount of rotations
        for i in range(rotations):
            time.sleep(60/self.speed)
            #print(f"{i} rotations")
        print(f"🏁 {self.name} finished riding")

    def race(self, other_bike):
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
tadej.ride()
jonas.ride()

print(tadej.race(jonas))

