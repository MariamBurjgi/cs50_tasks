import random

while True:
    level_str = input("Enter a level (positive integer): ")
    try:
        level = int(level_str)
        if level > 0:
            break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    guess_str = input("Guess the number (positive integer): ")
    try:
        guess = int(guess_str)
        if guess <= 0:
            raise ValueError
    except ValueError:
        continue

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break
