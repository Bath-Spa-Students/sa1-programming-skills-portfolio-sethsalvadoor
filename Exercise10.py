def check_even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    try:
        user_input = int(input("Enter a number: "))
        result = check_even_or_odd(user_input)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()
