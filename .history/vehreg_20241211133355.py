#Create a Python class Vehicle with attributes registration_number, type, and owner. 
#Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.
#Code Example: Provide a basic structure for the Vehicle class without methods.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

#- Expected Outcome: Completion of the Vehicle class with the update_ownermethod... 


    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner of vehicle {self.registration_number} has been update to {self.owner}!")

redvehicle = Vehicle("1234", "car", "Lynn Kade")
bluevehicle = Vehicle("5678", "suv", "Bridgette Waters")

# and a demonstration script showing the creation of Vehicle objects and updating their owners.

print(f"Red Vehicle Registration: {redvehicle.regisration_number}, Type: {redvehicle.type}, Owner: {bluevehicle.owner}")

print(f"Blue Vehicle Registration: {bluevehicle.regisration_number}, Type: {bluevehicle.type}, Owner: {bluevehicle.owner}")


#demonstrate changing the owner
redvehicle.update_owner("Linda Barker")

bluevehicle.update_owner("Brittany Pitts")

print(f"Updated Red Vehicle \nRegistration: {redvehicle.registration_number}, Type: {redvehicle.type}, Owner: {redvehicle.owner}")
