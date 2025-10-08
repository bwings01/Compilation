import MyMath

def maxnmin():
    num_1 = int(input("Enter number 1: "))
    num_2 = int(input("Enter number 2: "))
    print(f"Min is {MyMath.my_min(num_1, num_2)}")
    print(f"Max is {MyMath.my_max(num_1, num_2)}")
    print(f"Average is {MyMath.my_avg(num_1, num_2):.1f}")

if __name__ == "__main__":
    maxnmin()