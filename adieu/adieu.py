import inflect

def adieu(names):
    p = inflect.engine()
    length = len(names)
    if length == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif length == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        message = "Adieu, adieu, to "
        for i in range(length - 1):
            message += names[i] + ", "
        message += "and " + names[length - 1]
        print(message)

names = []
print("Enter names, one per line. Press ctrl-d when finished.")
while True:
    try:
        name = input()
        names.append(name)
    except EOFError:
        break
adieu(names)

