# Vanity Plates

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. Check length (min 2, max 6 characters)
    if not (2 <= len(s) <= 6):
        return False

    # 2. Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # 3. No periods, spaces, or punctuation allowed (only alphanumeric)
    if not s.isalnum():
        return False

    # 4. Number placement rules
    # Find the index of the first digit
    for i in range(len(s)):
        if s[i].isdigit():
            # The first number used cannot be a '0'
            if s[i] == "0":
                return False
            # All remaining characters from the first number must also be numbers
            if not s[i:].isdigit():
                return False
            break

    return True


if __name__ == "__main__":
    main()
