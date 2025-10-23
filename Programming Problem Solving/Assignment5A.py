# user input of integers and splits the numbers from the commas
nums = input("Enter numbers separated by commas: ").split(",")
# list strip to make sure the numbers are read as integers, extra at the end to loop through each item in nums, strips the empty spaces around them, and then filter out empty strings
intList = [int(x.strip()) for x in nums if x.strip() != ""]

def myselectionsort(intList):
    # makes the starting integer in the list the min index
    for i in range(len(intList)):
        min_index = i
        # goes through the rest of the list to find a smaller integer and make that the smallest integer and continues looping until it is finished with the whole list
        for j in range(i+1, len(intList)):
            if intList[j] < intList[min_index]:
                min_index = j
        # move the new found integer the beginning of the list. continues to shift list into the correct order
        intList[i], intList[min_index] = intList[min_index], intList[i]
    return intList
# storing my sorting method in sortedList variable
sortedList = myselectionsort(intList)
print("Sorted list (using my selection sort):", sortedList)
# storing python base sort function of the users list from outside the function
builtinSorted = sorted(intList)
print("Sorted list (using default function):", builtinSorted)

if sortedList == builtinSorted:
    print("Both lists are identical!")
else:
    print("The lists are not the same.")