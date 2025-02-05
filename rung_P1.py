import random
import string

# Define adjective and noun lists
adjectives = [
    "RAM", "Calm", "ROHAN", "KAISH", "ANKIT", "RAJ",
    "HaRRY", "Jolly", "KiSHAN", "LOVE", "MOHAN", "NISHA",
    "RAHUL", "RUBAN", "ALTAF", "ZISHAN", "ABJAN", "Bold"
]

nouns = [
    "Lion", "Falcon", "Phoenix", "Tiger", "Wolf", "Eagle",
    "Panther", "Dragon", "Bear", "Hawk", "Fox", "Shark",
    "Panda", "Knight", "Crusader", "Wizard", "Samurai", "Ninja"
]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, username_length=None):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    if include_numbers:
        username += str(random.randint(0, 9999))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    # Trim username if length is specified
    if username_length and username_length < len(username):
        username = username[:username_length]
    
    return username

# Function to save usernames to a file
def save_usernames_to_file(usernames, file_name="usernames.txt"):
    with open(file_name, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {file_name}.")

# Main program loop
def main():
    print("Welcome to the Random Username Generator!")
    
    # Get user preferences
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"
    username_length = input("Specify maximum username length (or press Enter to skip): ").strip()
    username_length = int(username_length) if username_length.isdigit() else None
    
    # Generate usernames based on preferences
    usernames = [
        generate_username(include_numbers, include_special_chars, username_length)
        for _ in range(num_usernames)
    ]
    
    # Display generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    # Option to save usernames
    save_option = input("\nWould you like to save these usernames to a file? (y/n): ").strip().lower()
    if save_option == "y":
        file_name = input("Enter the file name (default: usernames.txt): ").strip() or "usernames.txt"
        save_usernames_to_file(usernames, file_name)

    print("Thank you for using the Random Username Generator!")

# Run the program
if __name__ == "__main__":
    main()
