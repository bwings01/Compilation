def temperature_reading():
    temperatures = input("Enter temperatures in F (separate them with ,): ")
    temp_list = temperatures.split(",")
    temp_list_cleaned = []
    for t in temp_list:
        temp_list_cleaned.append(float(t.strip()))
    count = 0
    for _ in temp_list_cleaned:
        count += 1
    total = 0
    for temp in temp_list_cleaned:
        total += temp
    average = total / count
    print(f"You've entered {count} temperature points.")
    print(f"The average temperature is {average:.2f}F")
    return

if __name__ == "__main__":
    temperature_reading()