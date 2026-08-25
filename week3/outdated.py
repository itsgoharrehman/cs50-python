# Outdated

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date_str = input("Date: ").strip()

        # Format 1: M/D/YYYY
        if "/" in date_str:
            parts = date_str.split("/")
            if len(parts) == 3:
                try:
                    month = int(parts[0].strip())
                    day = int(parts[1].strip())
                    year = int(parts[2].strip())

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
                except ValueError:
                    pass

        # Format 2: Month Day, Year (comma is required)
        elif "," in date_str:
            try:
                month_day, year_str = date_str.split(",")
                year = int(year_str.strip())

                parts = month_day.strip().split()
                if len(parts) == 2:
                    month_name = parts[0].strip().title()
                    day = int(parts[1].strip())

                    if month_name in months and 1 <= day <= 31:
                        month = months.index(month_name) + 1
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
            except ValueError:
                pass


if __name__ == "__main__":
    main()
