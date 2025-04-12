def run_quiz():
    questions = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Sweden": "Stockholm",
        "Austria": "Vienna",
        "Greece": "Athens"
    }

    print("European Capitals Quiz! Let's begin.\n")

    score = 0
    for country, capital in questions.items():
        answer = input(f"What is the capital of {country}? ").strip().lower()
        if answer == capital.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {capital}.\n")

    print(f"You got {score} out of {len(questions)} correct!")

# Run the quiz
run_quiz()