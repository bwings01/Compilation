# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 2a

def madlib():
    name1 = input("Enter a name: ")
    name2 = input("Enter another name: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter a adverb: ")
    print(f"Once upon a time, there was a person named {name1} who had a child named {name2}. This child would {verb} {adverb} while singing to strangers.")
    return

if __name__ == "__main__":
    madlib()
