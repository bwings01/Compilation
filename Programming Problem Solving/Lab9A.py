def allMath(num1, num2):
    result = []

    # addition
    result.append(num1 + num2)

    # subtrataction
    result.append(num1 - num2)

    # multiplication
    result.append(num1 * num2)

    # division
    if num2 != 0:
        result.append(num1 / num2)
    else:
        result.append(None)

    # floor division
    if num2 != 0:
        result.append(num1 // num2)
    else:
        result.append(None)

    # modulus
    if num2 != 0:
        result.append(num1 % num2)
    else:
        result.append(None)

    # power
    result.append(num1 ** num2)
    
    return tuple(result)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print("Your resulting tuple is ", allMath(num1, num2))
