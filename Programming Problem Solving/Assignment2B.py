def escape_room():
    brass_key = 0
    iron_key = 0
    bed_check = 0
    while True:
        print("You wake up in a dimly lit room. The air smells faintly of dust and old wood. The only visible exit is a heavy iron door with a large lock. Looking around, you notice:\n- A small wooden chest sitting on a table in the corner\n- A bare mattress on the floor\n- A section of the floorboards that looks slightly uneven, almost as if one plane doesn't quite fit\n\nWhat do you do?\nA. Open the heavy iron door.\nB. Inspect the wooden chest\nC. Inspect the mattress.\nD. Inspect the suspicious plank in the floorboard.")
        choice = input()
        if choice == "A":
            if brass_key == 0 and iron_key == 0:
                print("You tug the handle. It doesn't budge. The key must be somewhere in this room...")
            elif brass_key == 1 and iron_key == 0:
                print("The brass key is too small for the door's lock. Maybe it opens something else.")
            elif iron_key == 1:
                print("The iron key slides into the lock. You turn it, the mechanism clicks. The door swings open. You're free!")
                break
        elif choice == "B":
            if brass_key == 0 and iron_key == 0:
                print("The chest is locked. The key has to be around here somewhere...")
            elif brass_key == 1 and iron_key == 0:
                iron_key = 1
                print("The brass key fits chest lock. It clicks open. Inside rests a heavier iron key. This one looks it is made for a door.")
            elif brass_key == 1 and iron_key == 1:
                print("You check the chest again, nothing else inside.")
        elif choice == "C":
            if bed_check == 0:
                print("You inspect the thin mattress, there is nothing on it. You lift it, there is nothing underneath either")
                bed_check = 1
            elif bed_check == 1:
                print("You already checked the mattress. There is nothing there.")
        elif choice == "D":
            if brass_key == 0:
                print("You pry up the loose plank. Hidden in the dust lies a small brass key.")
                brass_key = 1
            if brass_key == 1:
                print("You've already pried up the plank. There is nothing else underneath")
        else:
            print("Invalid Input!")
    return

if __name__ == "__main__":
    escape_room()