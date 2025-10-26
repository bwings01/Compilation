def main():
    while True:
        # main menu and data list setup
        print("Main Menu\n1. Enter letters\n2. Enter numbers\n3. Quit")
        choice = input("Enter your choice: ")
        data = []

        if choice == "1":
            # gets user input and inserts all inputs into the data list
            letters = input("Enter letters separated by commas: ").split(",")
            data = letters
            # printing the tuple
            print("Tuple: ",tuple(data))
            # defining the call of find_frequency and printing the dictionary
            freq = find_frequency(data)
            print(f"Frequency dictionary: {freq}")
            # defining the max frequency and matching it to all the elements that have the same frequency
            max_freq = max(freq.values())
            # list so that elements that are most frequent are separated and stored as final result
            max_freq_element = [key for key, value in freq.items() if value == max_freq]

            print(f"Most frequent elements: {max_freq_element}")
            print(f"Frequency: {max_freq}\n")

        elif choice == "2":
            # makes the numbers inputted by user into integers
            numbers = [int(x.strip()) for x in input("Enter numbers separated by commas: ").split(",")]
            data = numbers
            print("Tuple: ",tuple(data))
            freq = find_frequency(data)
            print(f"Frequency dictionary: {freq}")
            max_freq = max(freq.values())
            max_freq_element = [key for key, value in freq.items() if value == max_freq]
            print(f"Most frequent element(s): {max_freq_element}")
            print(f"Frequency: {max_freq}\n")
        
        elif choice == "3":
            print("Exiting program...")
            break
            
        else:
            print("Invalid input!")


def find_frequency(data):
    freq = {}
    # loops through the list data
    for element in data:
        # if the element exists already in the dictionary, then it will add 1 to the count after hitting said element in the list
        if element in freq:
            freq[element] += 1
        # if the element doesn't exist, the element is addedd to the dictionary and adds 1 to the count (value)
        else:
            freq[element] = 1
    return freq



if __name__ == "__main__":
    main()