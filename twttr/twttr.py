
    txt=input("Input: ").strip()

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for char in txt:
    if char  in vowels:
        txt = txt.replace(char, "")
print(txt)
