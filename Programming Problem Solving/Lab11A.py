# initialize class
class BuildingBlueprint:
    # constructor
    def __init__(self, stories: int, apartments: int, occupancy_rate: float):
        self.stories = stories
        self.apartments = apartments
        self.occupancy_rate = occupancy_rate
        
        # check if building is full
        if occupancy_rate == 1.0:
            self.is_full = True
        else:
            self.is_full = False
        
    # function for changing occupancy rate
    def update_occupancy(self, new_rate: float):
        self.occupancy_rate = new_rate
        if self.occupancy_rate == 1.0:
            self.is_full = True
        else:
            self.is_full = False

# set building objects
buildingOne = BuildingBlueprint(10, 20, 1.0)
buildingTwo = BuildingBlueprint(30, 30, .75)

# print initial building info
print(f"Year 2025:\nBuilding 1 has {buildingOne.stories} floors, {buildingOne.apartments} apartments, and is {buildingOne.occupancy_rate:.0%} occupied. Full? {buildingOne.is_full}\nBuilding 2 has {buildingTwo.stories} floors, {buildingTwo.apartments} apartments, and is {buildingTwo.occupancy_rate:.0%} occupied. Full? {buildingTwo.is_full}\n")

print("Many years passed\n")

# update building occupancy
buildingOne.update_occupancy(0.0)
buildingTwo.update_occupancy(1.0)

# print updated building info
print(f"Building 1 has {buildingOne.stories} floors, {buildingOne.apartments} apartments, and is {buildingOne.occupancy_rate:.0%} occupied. Full? {buildingOne.is_full}\nBuilding 2 has {buildingTwo.stories} floors, {buildingTwo.apartments} apartments, and is {buildingTwo.occupancy_rate:.0%} occupied. Full? {buildingTwo.is_full}\nLooks like people prefer taller buildings.")