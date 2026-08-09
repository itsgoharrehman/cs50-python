# Making Faces

def convert(text_msg):
    text_msg = text_msg.replace(":)", "🙂")
    text_msg = text_msg.replace(":(", "🙁")
    return text_msg

def main():
    user_input = input("Enter you msg: ")
    con_msg = convert(user_input)
    print(con_msg)

if __name__  == "__main__":
    main()