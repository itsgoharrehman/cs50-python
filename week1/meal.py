# Meal Time

def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if converted_time >= 7.00 and converted_time <= 8.00:
        print("breakfast time")
    elif converted_time >= 12.00 and converted_time <= 13.00:
        print("lunch time")
    elif converted_time >= 18.00 and converted_time <= 19.00:
        print("dinner time")
def convert(time):
    time = time.strip()
    hours, minutes = time.split(":")
    formatted_time = float(hours) + float(minutes) / 60.0
    return formatted_time

if __name__ == "__main__":
    main()
