# Just setting up my twttr

def main():
    # Prompt the user for input text
    text = input("Input: ")
    
    # Shorten the text by removing vowels
    result = shorten(text)
    
    # Output the result
    print(f"Output: {result}")


def shorten(word):
    vowels = "aeiouAEIOU"
    # Filter out characters that are in vowels
    return "".join([char for char in word if char not in vowels])


if __name__ == "__main__":
    main()
