# Dictionary mapping month numbers to the number of days
month_days = {
    1: 31,
    2: 28,  # Will adjust for leap year later
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user to input a month number
month = int(input("Enter the month number (1-12): "))

# Check if the input is valid
if 1 <= month <= 12:
    if month == 2:
        year = int(input("Enter the year: "))
        # Check if it's a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {month_days[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
