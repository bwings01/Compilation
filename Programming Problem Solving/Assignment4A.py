def format_word(word):
    return word.capitalize()

def convert_to_pascal_case(text):
    words = []
    word = ""
    for char in text:
        if char != " ":
            word += char
        else:
            if word != " ":
                words.append(format_word(word))
                word = ""
    if word != "":
        words.append(format_word(word))
    return "".join(words)

def main():
    text = input("Enter a string: ")
    pascal_case = convert_to_pascal_case(text)
    print("Pascal Case: ", pascal_case)

if __name__ == "__main__":
    main()

hello