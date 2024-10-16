# getting various classes from their respective files
# from vehicle import Vehicle
# from car import Car
# from Truck import Truck
class Garage():
    def __init__(self):
        # Constructor method initializes with no vehicle parked
        self.vehicle = None
     
    # parking a vehicle in the garage   
    def setVehicle(self, vehicle):
        self.vehicle = vehicle
    
    
    def tostring(self):
        if self.vehicle:  # If there's a vehicle parked, display its info
            return f"Description of the parked vehicle:\n {self.vehicle.tostring()}"
        else:  # show no vehicle in garage
            return "No vehicle is parked in the garage."   
 
        
# testing object of class Garage


# my_garage = Garage()

# print("Garage instances:")
# print(f"Initially, {my_garage.tostring()}")
# print()

# BMW = Car("Silver", has_winter_tires=True)
# my_garage.setVehicle(BMW)

# print("Parked Vehicle:")
# print(my_garage.tostring())




