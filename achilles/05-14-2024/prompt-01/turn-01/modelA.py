class Player:
    def __init__(self, name, strength, intelligence, agility):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility

def start_game():
    print("Welcome to Code Quest!")
    print("You are a young adventurer seeking fortune and glory in the land of Codeoria.")
    print("Your journey begins in the town of Variablesville, where you must declare your attributes.")

    name = input("What is your name? ")
    strength = int(input("What is your strength (1-10)? "))
    intelligence = int(input("What is your intelligence (1-10)? "))
    agility = int(input("What is your agility (1-10)? "))

    player = Player(name, strength, intelligence, agility)

    print(f"\nAh, {player.name}, you are indeed a brave adventurer!")
    print(f"Your strength is {player.strength}, your intelligence is {player.intelligence}, and your agility is {player.agility}.")

    choose_path(player)

def choose_path(player):
    print("\nYou stand at the crossroads of Variablesville. To the north lies the Forest of Loops,")
    print("to the east lies the Mountain of Conditional Statements, and to the west lies the Cave of Functions.")
    print("Which path will you choose?")

    choice = input("> ")

    if choice.lower() == "north":
        forest_of_loops(player)
    elif choice.lower() == "east":
        mountain_of_conditional_statements(player)
    elif choice.lower() == "west":
        cave_of_functions(player)
    else:
        print("Invalid choice. Please try again.")
        choose_path(player)

def forest_of_loops(player):
    # TO DO: Implement the Forest of Loops challenge
    pass

def mountain_of_conditional_statements(player):
    # TO DO: Implement the Mountain of Conditional Statements challenge
    pass

def cave_of_functions(player):
    # TO DO: Implement the Cave of Functions challenge
    pass

start_game()