"""
    Prompt: Write a Python function that takes a list of integers and returns the sum of the elements in the list. 
    The function should be named sum_of_elements.
"""

def modelA():
    def sum_of_elements(integer_list):
        total = 0

        # Loop through each element in the list and add it to the total
        for element in integer_list:
            total += element

        return total
    
    return sum_of_elements([1, 2, 3, 4, 5]) # 15

def modelB():
    def sum_of_elements(list_of_numbers):
        total = 0
        for number in list_of_numbers:
            total += number
        return total

    print(sum_of_elements([1, 2, 3, 4, 5]))

print("Model A:")
print(modelA())
print()

print("Model B:")
modelB()
print()