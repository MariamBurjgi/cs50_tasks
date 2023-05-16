def main ():
    text = input ("Post anything: ")
    novowels = without_vowels(text)
    print(novowels)



def without_vowels(text):
    vowels = "aeiouAEIOU"
    novowels = ""
    for char in text:
         if char not in vowels:
             novowels = novowels + char
    return novowels


if __name__ == "__main__":
     main()
