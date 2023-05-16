story = input ("Please, tell us about your story")
symbols = len(story)

if symbols == 0:
    print("Enter text, please")
else:
    print(f"You have", symbols, "symbols")
