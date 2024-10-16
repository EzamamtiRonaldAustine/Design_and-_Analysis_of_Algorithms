from Truck import Truck
from Garage import Garage
class GarageTester:
    # Method to create an example of a Truck parked in a Garage
    def getExample(self):
        truck = Truck("black")
        garage = Garage() #Garage instance
        garage.setVehicle(truck) # Park the truck in the garage
        return garage.tostring()
    

print("Garage-Tester section:")
tester = GarageTester()
vehicle_in_garage = tester.getExample()
print(vehicle_in_garage)

