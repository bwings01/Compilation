def letterfreqquiz():
    sentence = input("Enter a sentence (lowercase letters only): ")
    print("\n" * 50)
    letters = ""
    counts = ""
    index = 0
    while index < len(sentence):
        char = sentence[index].lower()
        if char.isalpha():
            found = False
            position = 0
            while position < len(letters):
                if letters[position] == char:
                    current = int(counts[position])
                    counts = counts[:position] + str(current + 1) + counts[position + 1:]
                    found = True
                    break
                position += 1
            if not found:
                letters += char
                counts += "1"
        index += 1
    guessed_letters = ""
    while len(guessed_letters) < len(letters):
        position = 0
        while position < len(letters):
            char = letters[position]
            if char in guessed_letters:
                position += 1
                continue
            guess = input(f"Guess the frequency of letter '{char}': ")
            try:
                guess_number = int(guess)
            except ValueError:
                print("Invalid input\n")
                continue
            actual = int(counts[position])
            if guess_number < actual:
                print("Too low!\n")
            elif guess_number > actual:
                print("Too high!\n")
            else:
                print("Correct!\n")
                guessed_letters += char
            position += 1
    print("Congratulations! You completed the quiz.\n")

if __name__ == "__main__":
    letterfreqquiz()