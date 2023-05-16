while True:
    try:
        x, y = input("Enter fuel gauge fraction (X/Y): ").split("/")
        x = int(x)
        y = int(y)
        if y == 0 or x > y:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please try again.")

percentage = round(x / y * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print("{}%".format(percentage))
