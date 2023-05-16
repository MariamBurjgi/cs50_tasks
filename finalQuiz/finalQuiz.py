def main():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to the online quiz.")
    ready = input("Are you ready to start? (y/n) ")
    if ready.lower() == "y":
        quiz_questions()
        quiz_scoring(name)
        quiz_results(name)
    else:
        print("Okay, come back when you're ready.")
def quiz_questions():
    questions = ["What is the capital of France?", "What is the largest mammal in the world?", "What is the symbol for potassium?"]
    answers = ["paris", "blue whale", "k"]
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        answer = input("Answer: ")
        if answer.lower() == answers[i]:
            score += 1
    return score
def quiz_scoring(name, score):
    percentage = (score / 3) * 100
    print(f"Well done, {name}! You scored {score} out of 3, which is {percentage}%.")
    if percentage >= 80:
        print("You're a quiz master!")
    elif percentage >= 50:
        print("Not bad, but there's room for improvement.")
    else:
        print("Better luck next time!")
def quiz_results(name, score):
    with open("quiz_results.txt", "a") as file:
        file.write(f"{name}: {score}\n")
if __name__ == "__main__":
    main()
