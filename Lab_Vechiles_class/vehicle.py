class Vehicle():
    def __init__(self, color):
        self.color = color  #instance attribute color 
    
    def getColor(self):
        # Returns the value of the color attribute
        return self.color
     
    # Method to return a string description of the vehicle   
    def tostring(self):
        return(f"The vehicle is painted: {self.color}")
        
               
#object of class Vehicle 
print("Objects of class Vehicle:")      
vehicle_1 = Vehicle("blue")
print(vehicle_1.tostring())
print()
#getting the vehicle color
print(vehicle_1.getColor())
print()



    

        