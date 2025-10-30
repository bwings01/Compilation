# create chair class
class Chair:
    def __init__(self, numOfLeg: 4, rolling: False, material: str = "wood"):
        # attribute defaults
        self.numOfLeg = numOfLeg
        self.rolling = rolling
        self.material = material

# function to ask user for their chair attributes
def main():
    print("You are about to create a chair.")
    numOfLeg = int(input("How many legs does your chair have: "))
    rolling = input("Is your chair rolling (true/false): ")
    material = input("What is your chair made of: ")

    # check if chair is already default settings defined by our class
    if  numOfLeg == 4 and rolling.lower() == False and material.lower() == "wood":
        print("Your cahir has 4 legs, is not rolling, and is made of wood.")

    # if not default, force to default
    else:
        # create chair object with usr input
        chair = Chair(numOfLeg, rolling.lower() == "true", material.lower())
        print(f"Your chair has {chair.numOfLeg} legs, is {'rolling' if chair.rolling else 'not rolling'}, and is made of {chair.material}.")
        print("This program is going to change that.")
        # force reset to default values
        chair.numOfLeg = 4
        chair.rolling = False
        chair.material = "wood"
        # print out the default chair attributes
        print(f"Your chair has {chair.numOfLeg} legs, is {'rolling' if chair.rolling else 'not rolling'}, and is made of {chair.material}.")



if __name__ == "__main__":
    main()