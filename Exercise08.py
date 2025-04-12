# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Optional: Let the user enter the search term
search_term = input("Enter the name to search for: ").strip()

# Search for the name in the list
if search_term in names:
    print(f"{search_term} was found in the list!")
else:
    print(f"{search_term} was NOT found in the list.")
