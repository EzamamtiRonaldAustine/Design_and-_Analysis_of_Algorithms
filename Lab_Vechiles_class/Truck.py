#getting the class Vehicle
from vehicle import Vehicle
# class Truck is child of class Vehicle 
class Truck(Vehicle):
    def __init__(self, color, has_trailer=False):
        #the superclass (Vehicle) constructor sets the color
        super().__init__(color)
        self.has_trailer = has_trailer
        
    # Overriding the tostring method using the super keyword
    def tostring(self):
        return super().tostring() + f"\n The truck has a trailer: {self.has_trailer} "


#objects of class Truck
print("Objects of class Truck:")
monster_truck = Truck("blazing_red", True)    
construction_truck = Truck("Yellow")
print(construction_truck.tostring())
print(monster_truck.tostring())
print()