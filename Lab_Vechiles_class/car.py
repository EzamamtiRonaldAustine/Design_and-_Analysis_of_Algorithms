#getting the class Vehicle
from vehicle import Vehicle

# class Car is child of class Vehicle 
class Car(Vehicle):
    def __init__(self, color, has_winter_tires =False ):
        #the superclass (Vehicle) constructor sets the color
        super().__init__(color)
        self.has_winter_tires =  has_winter_tires
        
    # Overriding the tostring method to include information about winter tires using super
    def tostring(self):
        return super().tostring() + f", It has winter tires: {self.has_winter_tires}"
    
#objects of class Car
print("Objects of class Car:")
mustang = Car("Black", True)
tesla =  Car("Red")

print(mustang.tostring())
print(tesla.tostring())
print()

