def pyramid():
    word = input("Enter a string: ")
    word = word.replace(" ", "")
    for i in range(1, len(word) + 1):
        print(word[:i])
    return

if __name__ == "__main__":
    pyramid()