# Step 1: Get user input and store it in variables
name = input("Enter your full name (e.g., John Smith): ")
hometown = input("Enter your hometown: ")

# Step 2: Try converting age to integer, handle if user enters a non-numeric value
age_input = input("Enter your age: ")
try:
    age = int(age_input)
except ValueError:
    print("Invalid age. Please enter a numeric value.")
    exit()  # Stop the program if age is not a valid number

# Step 3: Store data in a dictionary
user_info = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

# Step 4: Print all values on separate lines using a single print() statement
print(f"{user_info['Name']}\n{user_info['Hometown']}\n{user_info['Age']}")
