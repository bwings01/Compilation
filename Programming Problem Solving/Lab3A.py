# Class: CSE 1321L
# Section: W03
# Term: Fall
# Instructor: Milo Wilson
# Name: Braeden Wings
# Lab: 3a

def creditcard():
    current_balance = float(input("Amount owed: "))
    annual_percentage_rate = float(input("$APR: "))
    monthly_percentage_rate = annual_percentage_rate / 12
    minimum_payment = current_balance * (monthly_percentage_rate / 100)
    print(f"Monthly percentage rate: {round(monthly_percentage_rate, 3)}")
    print(f"Minimum payment: ${round(minimum_payment, 2)}")
    return

if __name__ == "__main__":
    creditcard()