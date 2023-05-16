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

def main():
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

if __name__ == "__main__":
    main()
