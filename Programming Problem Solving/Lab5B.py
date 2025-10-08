# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 5b

def box_triangle():
  size = int(input("Please enter a value for the size: "))

  print(f"This is the requested {size}x{size} box: ")
  for i in range(size):
      for j in range(size):
          print("*", end="")
      print()

  print(f"This is the requested right-facing {size}x{size} right-triangle: ")
  for i in range(1, size+1):
      for j in range(i):
          print("*", end="")
      print()

  print(f"This is the requested left-facing {size}x{size} right-triangle:")
  for i in range(1, size + 1):
      for j in range(size - i):
          print(" ", end="")
      for j in range(i):
          print("*", end="")
      print()
  return

if __name__ == "__main__":
     box_triangle()