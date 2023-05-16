def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s[2:].isalnum():
        return False
    if s[2:].isdigit() and s[2] == '0':
        return False
    if any(c in s[2:-1] for c in '0123456789'):
        return False
    return True

plate = input("Enter your vanity plate: ")
if is_valid(plate):
    print("Valid")
else:
    print("Invalid")



main()