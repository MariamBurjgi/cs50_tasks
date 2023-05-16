def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower().strip()
    print (answer(user_input))

def answer(txt):
    if txt == "42" or txt =="forty-two" or txt =="forty two":
        return"yes"
    else:
        return"no"

main()
