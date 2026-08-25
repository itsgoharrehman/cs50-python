# Fuel Gauge

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x_str, y_str = fraction.split("/")
            x = int(x_str)
            y = int(y_str)

            # Ensure non-negative X, positive Y, and X not greater than Y
            if x < 0 or y <= 0 or x > y:
                continue

            percentage = round((x / y) * 100)
            break
        except (ValueError, ZeroDivisionError):
            continue

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
