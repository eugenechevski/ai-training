def start_game():
    print("Welcome to the Python Adventure Game!")
    name = input("Enter your character's name: ")
    print(f"Hello, {name}! Your adventure begins now.")
    path = []
    while True:
        choice = input("Do you want to go left or right? (left/right): ").strip().lower()
        if choice == "left" or choice == "right":
            print("You chose to go " + choice + ".")
            path.append(choice)
            if len(path) > 5:
                break
        else:
            print("Invalid choice. Please choose left or right.")
    display_progress(path)

def display_progress(path):
    print("\nYour journey has come to an end.")
    print("Here's a summary of your path:")
    for i, choice in enumerate(path):
        print(f"{i+1}. You went {choice}.")

start_game()