def divCalc():
    print("[Division]")
    while True:
        # basic interation for calculator
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2
            print(f"{num1}/{num2} = {result:.2f}")
        # catching exceptions
        except ValueError:
            print("Please enter numberical values.")
        except ZeroDivisionError:
            print("We cannot divide by zero.")
        # "finally:" = will execute this block no matter what happens in the try block
        finally:
            # user input to continue or exit
            choice = input("Would you like to perform another division (Y/N)?: ").strip().upper()
            if choice == 'Y':
                continue
            else:
                break


if __name__ == "__main__":
    divCalc()