# Define the correct password
correct_password = "12345"

# Set the maximum number of attempts
max_attempts = 5
attempts = 0

# Start the loop to prompt for password
while attempts < max_attempts:
    user_input = input("Enter your password: ")
    if user_input == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
