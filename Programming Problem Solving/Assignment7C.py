def get_scores():
    scores = []
    try:
        num_students = int(input("Enter number of students: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return get_scores()
    # for the number of students, get each score
    for i in range(1, num_students + 1):
        while True:
            try:
                score = int(input(f"Enter score for student {i}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Error: Score must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter an integer score.")
    return scores

# analyze scores
def analyze_scores(scores):
    high = max(scores)
    low = min(scores)
    avg = sum(scores) / len(scores)
    passed = 0
    failed = 0

    for score in scores:
        if score >= 60:
            passed += 1
        else:
            failed += 1

    return high, low, avg, passed, failed


def display_results(high, low, avg, passed, failed):
    print("--- Score Report ---")
    print(f"Highest score: {high}")
    print(f"Lowest score: {low}")
    print(f"Average score: {avg:.1f}")
    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")


def main():
    # get scores
    scores = get_scores()
    # analyze scores
    high, low, avg, passed, failed = analyze_scores(scores)
    # run display
    display_results(high, low, avg, passed, failed)


if __name__ == "__main__":
    main()