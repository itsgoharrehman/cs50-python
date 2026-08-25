# Grocery List

def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().upper()
            if not item:
                continue
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            for item in sorted(grocery_list.keys()):
                print(f"{grocery_list[item]} {item}")
            break


if __name__ == "__main__":
    main()
