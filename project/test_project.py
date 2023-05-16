import unittest
from project import calculate_bmi


from project import calculate_bmi

def test_calculate_bmi():
    # Test with valid values
    assert calculate_bmi(70, 1.75) == 26.289447243328066

    # Test with zero values
    try:
        calculate_bmi(0, 0)
    except ValueError as e:
        assert  "Please, write weight and height in positive values."

    # Test with negative values
    try:
        calculate_bmi(-70, 1.75)
    except ValueError as e:
        assert  "Please, write weight and height in positive values."


#def test_function_2()
#import unittest
from project import calculate_calories


def test_calculate_calories_male():
        weight = 80  # kg
        height = 180  # cm
        age = 30  # years
        gender = 'male'
        assert calculate_calories (weight, height, age, gender) == 1853.36

def test_calculate_calories_female():
        weight = 60  # kg
        height = 160  # cm
        age = 25  # years
        gender = 'female'
       # expected_bmr = 1370.7
        assert calculate_calories (weight, height, age, gender) == 1388.1


def test_calculate_calories_negative_values():
        weight = -70  # kg
        height = 170  # cm
        age = 40  # years
        gender = 'male'
        assert ValueError
        assert calculate_calories(weight, height, age, gender) == -261.64

if __name__ == '__main__':
    unittest.main()

   # import unittest


from project import generate_workout_plan


def test_workout_plan():
        num_weeks = 4
        days_per_week = 3
        workout_plan = generate_workout_plan(num_weeks, days_per_week)

        # Check if the number of sessions is correct
        assert len(workout_plan), num_weeks * days_per_week

        # Check if each session has at least one strength exercise
        for session in workout_plan:
            assert len (session[0])

        # Check if each session has at least one cardio exercise
        for session in workout_plan:
            assert len (session[1])

        # Check if the exercises in each session are valid
        strength_exercises = ['push-ups', 'squats', 'lunges', 'dumbbell rows', 'dumbbell curls', 'bench press']
        cardio_exercises = ['running', 'cycling', 'jumping jacks', 'burpees', 'jump rope', 'stair climbing']
        for session in workout_plan:
            for exercise in session[0]:
                assert exercise, strength_exercises
            for exercise in session[1]:
                assert exercise, cardio_exercises

if __name__ == '__main__':
    unittest.main()

















