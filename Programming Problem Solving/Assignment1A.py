def isValid():
    while True:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        if width + height > 30:
            print("This is a valid rectangle.")
            area = areacalc(width, height)
            perimeter = perimetercalc(width, height)
            print(f"The area is: {area:.1f}")
            print(f"The perimeter is: {perimeter:.1f}")
            end = input("Do you want to enter another width and height (Y/N)?:\n ")
            if end == "Y":
                continue
            elif end == "N":
                break
            else:
                print("Invalid input.")
        else:
            print("This is an invalid rectangle.")
            return False

def areacalc(width, height):
    return width * height
def perimetercalc(width, height):
    return 2 * (width + height)

if __name__ == "__main__":
    isValid()
