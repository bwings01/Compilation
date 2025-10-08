def weight_conversion():
    weight_kg = int(input("Enter weight in kilograms: "))

    weight_lbs = weight_kg*2.20462
    stones = int(weight_lbs//14)
    remaining_lbs = weight_lbs % 14

    print(f"{weight_kg:.1f} kilograms is approximately {stones} stones and {remaining_lbs:.2f} pounds.")
    return


if __name__ == '__main__':
    weight_conversion()