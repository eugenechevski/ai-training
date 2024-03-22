def greet(name, message):
    print(f"Hello, {name}! {message}")

# Calling the function with keyword arguments
greet(name="Alice", message="Nice to meet you") 

def calculate_area(length, width, height=1):  # height has a default value of 1
    volume = length * width * height
    return volume

# Using keyword arguments selectively
area1 = calculate_area(length=5, width=3)  # height will use the default
area2 = calculate_area(5, 2, height=4)  # height is overridden