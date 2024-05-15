# Introduction to the game
print("Welcome to Code Quest!")
print("You are a young programmer who has been transported to a mystical world.")
print("Your coding skills are the only way to survive.")

# Ask player to set their character's name
character_name = input("What is your character's name? ")

# Ask player to set their character's attributes
print("Choose your character's attributes:")
print("1. Strength (1-10)")
print("2. Intelligence (1-10)")
print("3. Agility (1-10)")

strength = int(input("Enter strength: "))
intelligence = int(input("Enter intelligence: "))
agility = int(input("Enter agility: "))

# Print out the character's information
print(f"Name: {character_name}")
print(f"Strength: {strength}")
print(f"Intelligence: {intelligence}")
print(f"Agility: {agility}")

# Present the player with choices
print("You find yourself standing in front of a dense forest.")
print("Do you:")
print("1. Enter the forest")
print("2. Search for a village")
print("3. Follow a nearby stream")

choice = input("Enter your choice: ")

# Handle the player's choice
if choice == "1":
    print("You enter the forest and come across a clearing.")
    # Add more code here to continue the story
elif choice == "2":
    print("You search for a village and find one after a few hours of walking.")
    # Add more code here to continue the story
elif choice == "3":
    print("You follow the stream and find a hidden waterfall.")
    # Add more code here to continue the story
else:
    print("Invalid choice. Please try again.")