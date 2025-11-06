# initializing classes
class Car:

    def __init__(self, make: str, model: str, year: int, per_day_rate: int):
        # attributes
        self.make = make
        self.model = model
        self.year = year
        self.per_day_rate = per_day_rate
        # is rented attribute for tracking rental status
        self.isRented = False

    # method for availability
    def is_available(self):
        return self.isRented
    
    # method for renting
    def set_rented(self, days: int):
        self.isRented = True
        print(f"{self.year} {self.make} {self.model} has been rented for {days} days.\nCustomer will be charge ${self.per_day_rate * days:.2f} at return\n")
    
    # method for returning
    def set_returned(self):
        self.isRented = False
        

    # method for car info
    def info(self):
        if self.isRented == False:
            status = "AVAILABLE, "
            rate = f"PER DAY RATE: ${self.per_day_rate}"
        else:
            status = "Rented"
            rate = ""
        return f"{self.year} {self.make} {self.model} - {status}{rate}"

class OwlRental:

    def __init__(self, depot: list):
        # attributes
        self.depot = depot

    # method for adding car to depot
    def add_car(self, make: str, model: str, year: int, per_day_rate: int):
        car = Car(make, model, year, per_day_rate)
        self.depot.append(car)

    # method for listing cars
    def list_cars(self):
        for i, car in enumerate(self.depot):
            print(f"{i} - {car.info()}")

    # method for renting
    def rent_car(self, index: int, days: int):
        car = self.depot[index]
        if car.is_available() == False:
            car.set_rented(days)
        else:
            print("Error: Car is already rented\n")

    # method for returning
    def return_car(self, index: int):
        car = self.depot[index]
        if car.is_available() == False:
            print("Error: Car is not rented\n")
        else:
            car.set_returned()
            print(f"{car.year} {car.make} {car.model} has been returned\n")

def main():

    # create rental depot
    depot = []
    rental = OwlRental(depot)

    # add cars to depot
    rental.add_car("Toyota", "Corolla", 2025, 49.99)
    rental.add_car("Honda", "Civic", 2023, 45.50)
    rental.add_car("Tesla", "Model 3", 2023, 119.00)

    print("[Owl Rent-a-Car]")

    # main loop
    while True:
        print("1. Rent\n2. Return\n3. View Cars\n4. Exit")

        choice = int(input("> "))

        # renting
        if choice == 1:
            print("")
            rental.list_cars()
            index = int(input("Select an index: "))
            days = int(input("How many day(s)?: "))
            rental.rent_car(index, days)

        # returning
        elif choice == 2:
            print("")
            rental.list_cars()
            index = int(input("Select an index: "))
            rental.return_car(index)
        
        # view cars
        elif choice == 3:
            print("")
            rental.list_cars()
            print("")

        # exit
        elif choice == 4:
            break


if __name__ == "__main__":
    main()