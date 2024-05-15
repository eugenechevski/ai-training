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
            if len(path) >= 5:
                print("Congratulations, you have reached the endpoint!")
                track_progress(path)
                break
        else:
            print("Invalid choice. Please choose left or right.")

def track_progress(path):
    print("Your journey:")
    for i, step in enumerate(path):
        print(f"Step {i+1}: {step}")

start_game()