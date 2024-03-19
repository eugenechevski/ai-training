def print_details(name, age, **other_info):
    print("Name:", name)
    print("Age:", age)

    for key, value in other_info.items():
        print(key, ":", value)

# Calling the function with keyword arguments:
print_details("Alice", 30, city="New York", occupation="Software Engineer")

def calculate(num1, num2, operation="add"):  # operation has a default value
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    else:
        return "Invalid operation"

# Using positional and keyword arguments
result = calculate(10, 5, operation="multiply")  
print(result)  # Output: 50