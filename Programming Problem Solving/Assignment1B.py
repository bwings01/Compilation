def energy_consumption_calculator():
    voltage = int(input("Enter the voltage (in volts): "))
    resistance = int(input("Enter the resistance (in ohms): "))
    time = int(input("Enter the time (in hours): "))
    CONVERSION_FACTOR = 1000

    energy = (voltage**2 * time)/(resistance * CONVERSION_FACTOR)

    print(f"The device consumed {energy:.2f} kWh of energy.")
    return

if __name__ == '__main__':
    energy_consumption_calculator()