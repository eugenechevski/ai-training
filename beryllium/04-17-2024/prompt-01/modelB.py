import random

def roll_dice(num_dice=1):
    total_sum = 0 ; 
    for _ in range(num_dice):
        #random.randint(1,6) generates a random number between 1 and 6(inclusive)
        total_sum += random.randint(1,6)
    return total_sum

#Example usage:
print(roll_dice(4))  #Simulate rolling 4 dices and print the sum