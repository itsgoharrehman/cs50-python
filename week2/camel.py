# camelCase

def main():
    # Prompt the user for a variable name in camel case
    camel_case = input("camelCase: ")
    
    # Initialize a list to build the snake case version
    snake_case = []
    
    # Iterate through each character in the camel case string
    for char in camel_case:
        # If the character is uppercase, prepend an underscore and convert to lowercase
        if char.isupper():
            snake_case.append("_" + char.lower())
        else:
            # Otherwise, append the character as it is
            snake_case.append(char)
            
    # Join the list into a string and print it
    print("".join(snake_case))


if __name__ == "__main__":
    main()
