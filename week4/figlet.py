# Frank, Ian and Glen's Letters

import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        # Zero command-line arguments: select a random font
        font = random.choice(fonts)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        # Two command-line arguments: set specified font
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
