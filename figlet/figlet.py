import sys
import random
from pyfiglet import Figlet

if len(sys.argv) == 1:
    # If no arguments provided, choose a random font
    fonts = Figlet().getFonts()
    font = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    # If two arguments provided and the first is -f or --font, use the specified font
    font = sys.argv[2]
else:
    # If arguments provided are invalid, exit with an error message
    sys.exit("Usage: python figlet.py [-f|--font FONT]")

# Set the chosen font
figlet = Figlet(font=font)

# Prompt the user for input
text = input("Enter some text: ")

# Output the input in the chosen font
print(figlet.renderText(text))
