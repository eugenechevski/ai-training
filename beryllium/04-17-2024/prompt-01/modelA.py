import random


def roll_dice(num_dice=1):
    total_sum = 0
    for _ in range(num_dice):
        # since dices have faces from 1 to 6, we use randint(1,6)
        total_sum += random.randint(1, 6)
    return total_sum


# testing
print(roll_dice())  # output will be between 1 and 6
print(roll_dice(4))  # output will be between 4 and 24 (sum of 4 dice rolls)
