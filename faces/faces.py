def main():
    txt = input("write your text: ")
    txt = convert(txt)
    print (txt)



def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()