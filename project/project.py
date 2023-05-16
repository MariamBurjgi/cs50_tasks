import random


def main():

    print("Welcome to Fitness Instructor!")
    while True:
        print("Please choose an option:")
        print("1. Calculate BMI")
        print("2. Calculate daily calorie intake recommendation")
        print("3. Generate a workout plan")
        print("4. Quit")
        choice = input()
        if choice == "1":
         weight = float(input("Enter your weight in kilograms: "))
         height = float(input("Enter your height in meters: "))
         bmi = calculate_bmi(weight, height)
         print("Your BMI is:", bmi)


        if choice == "2":
     # Get user input for weight, height, age, and gender
            weight_kg = float(input("Enter your weight in kilograms: "))
            height_cm = float(input("Enter your height in centimeters: "))
            age_years = int(input("Enter your age in years: "))
            gender = input("Enter your gender (male or female): ")

    # Convert height from cm to meters
            height_m = height_cm / 100

    # Calculate daily calorie needs (BMR)
            bmr = calculate_calories(weight_kg, height_m, age_years, gender)

    # Print result
            print("Your daily calorie needs (BMR) are:", bmr)

        if choice == "3":
                # Get user input for number of weeks and days per week
            num_weeks = int(input("Enter the number of weeks for your workout plan: "))
            days_per_week = int(input("Enter the number of days per week for your workout plan: "))

    # Generate workout plan

            workout_plan = generate_workout_plan(num_weeks, days_per_week)

    # Print workout plan
            print("Your workout plan for the next", num_weeks, "weeks:")
            for session in workout_plan:
                print("Session", ":")
                print("Strength exercises:", session[0])
                print("Cardio exercises:", session[1])
                print()

        if choice == "4":
            print("Welcome to the question-answering program!")
            ask_about_exit()




#def function_1():
def calculate_bmi(weight, height):

    """  This function calculates the Body Mass Index (BMI) based on the given weight and height."""

    if weight <= 0 or height <= 0:
        raise ValueError("Please, write weight and height in positive values.")
    bmi = weight / (height ** height)
    return bmi


#def function_2():
def calculate_calories(weight, height, age, gender):
    """
    Calculates daily calorie needs (BMR) based on weight, height, age, and gender.
    Weight should be in kilograms (kg), height should be in centimeters (cm), and age should be in years.
    Gender should be either 'male' or 'female'.
    """
    if gender.lower() == 'male':
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    return bmr


#def function_n():
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

def ask_about_exit():
    while True:
        answer = input("Are you sure you want to exit? ")
        if answer.lower() in ['yes','of course','sure' ]:
            print("Goodbye!")
            break
        else:
            print("You asked: ", answer)

if __name__ == "__main__":
    main()