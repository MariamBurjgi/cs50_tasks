def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
      if not s[:2].isalpha():
           return False
      if len(s) <2 or len(s) >6:
          return False
      if not s[2:].isalnum():
        return False
      if s[2:].isdigit() and s[2] == '0':
        return False
      if not s[2:-1].isalpha():
        return False
      else:
        return true

main()





