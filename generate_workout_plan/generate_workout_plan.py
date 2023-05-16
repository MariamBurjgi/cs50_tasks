import random

def generate_workout_plan(num_weeks, days_per_week):
    # List of available strength exercises
    strength_exercises = ['push-ups', 'squats', 'lunges', 'dumbbell rows', 'dumbbell curls', 'bench press']
    # List of available cardio exercises
    cardio_exercises = ['running', 'cycling', 'jumping jacks', 'burpees', 'jump rope', 'stair climbing']
    # Determine total number of workout sessions
    num_sessions = num_weeks * days_per_week

    # Initialize empty list to store workout sessions
    workout_plan = []
    # Generate workout plan for each session
    for i in range(num_sessions):
        # Choose strength exercises randomly
        num_strength_exercises = random.randint(1, 3)
        strength_session = random.sample(strength_exercises, num_strength_exercises)

        # Choose cardio exercises randomly
        num_cardio_exercises = random.randint(1, 2)
        cardio_session = random.sample(cardio_exercises, num_cardio_exercises)

        # Append session to workout plan
        workout_plan.append((strength_session, cardio_session))

    return workout_plan

def main():
    # Get user input for number of weeks and days per week
    num_weeks = int(input("Enter the number of weeks for your workout plan: "))
    days_per_week = int(input("Enter the number of days per week for your workout plan: "))

    # Generate workout plan
    workout_plan = generate_workout_plan(num_weeks, days_per_week)

    # Print workout plan
    print("Your workout plan for the next", num_weeks, "weeks:")
    for i, session in enumerate(workout_plan):
        print("Session", i+1, ":")
        print("Strength exercises:", session[0])
        print("Cardio exercises:", session[1])
        print()

if __name__ == "__main__":
    main()
