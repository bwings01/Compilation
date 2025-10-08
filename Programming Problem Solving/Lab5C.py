# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 5c

def please_loop():
    while True:
        user_input = input('If you would like to stop this program, say "please": ')
        if user_input == "please":
            print("Program complete")
            break
    return

if __name__ == "__main__":
    please_loop()