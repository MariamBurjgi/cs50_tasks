def ask_about_exit():
    while True:
        answer = input("Are you sure you want to exit? ")
        if answer.lower() in ['yes','of course','sure' ]:
            print("Goodbye!")
            break
        else:
            print("You asked: ", answer)

def main():
    print("Welcome to the question-answering program!")
    ask_about_exit()

if __name__ == "__main__":
    main()
