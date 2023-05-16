import re


def validate(ip):
    # Check if the string matches the pattern for an IPv4 address
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)

    if not match:
        return False

    # Convert each group to an integer and check if it's within the valid range
    for group in match.groups():
        if not (0 <= int(group) <= 255):
            return False

    return True