def sumofproducts():
    n = int(input("Enter a number: ").strip())
    total = 0
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            product = i * j
            duplicate = False
            a = 1
            while a <= i:
                if a < i:
                    b_max = n
                else:
                    b_max = j - 1
                b = 1
                while b <= b_max:
                    if a * b == product:
                        duplicate = True
                        break
                    b += 1
                if duplicate:
                    break
                a += 1
            print(f"({i},{j}) = {product}", end="")
            if duplicate:
                print(" (duplicate, ignore)")
            else:
                print()
                total += product
            j += 1
        i += 1
    print(f"Sum of unique products: {total}")
    return

if __name__ == "__main__":
    sumofproducts()