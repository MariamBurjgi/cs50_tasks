#FITNESS INSTRUCTOR APP

Video Demo: <https://studio.youtube.com/channel/UCKf_PMp-yeRvVPR7nAejKfw/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D>

##DESCRIPTION:
    The final project for CS50 Python is a program called Fitness Instructor that offers three main features:
   calculating the user's BMI, recommending daily calorie intake, and generating a workout plan.
   It counts BMI(the Body Mass Index), calories and generates workout_plan, based on fitness level

##Functions and Libraries:
   main(): The main function that runs the program and presents the user with a menu of options.
   calculate_bmi(weight, height): A function that calculates the body mass index (BMI) based on the user's weight and height.
   calculate_calories(weight, height, age, gender): A function that calculates the user's daily calorie needs (BMR),
 based on their weight, height, age, gender.
   generate_workout_plan(num_weeks, days_per_week): A function that generates a workout plan for the user based on the number of weeks and days
per week they specify.
   ask_about_exit(): A function that prompts the user if they want to exit the program and exits if the user confirms.


##Library:
    random: A library used for generating random numbers and making random selections from lists. It is used to generate a randomized
workout plan for the user.

#TESTS:
  test_calculate_bmi
  test_calculate_calories_male
  test_calculate_calories_female
  test_calculate_calories_negative_values
  test_workout_plan

Library:
   The code appears to use the built-in unittest library, which is a testing framework in Python used for unit testing. It is used
to define unit test cases and make assertions about expected outcomes. The unittest library provides a set of tools for constructing
and running tests.


