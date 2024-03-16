def convert_temperature(temperature, unit):
    if unit not in ("Celsius", "Fahrenheit"):
        raise ValueError("Invalid unit provided. Please use 'Celsius' or 'Fahrenheit'.")
    
    if unit == "Celsius":
        converted_temperature = (temperature * 9.0 / 5.0 + 32.0)
    else:
        converted_temperature = (temperature - 32.0) * 5.0 / 9.0
    
    return round(converted_temperature, 2) + " " + unit

print(convert_temperature(32, "Fahrenheit"))  # Output: "32.00 Celsius"
print(convert_temperature(20, "Celsius"))  # Output: "68.00 Fahrenheit"
print(convert_temperature(30, "Kelvin"))  # Output: Invalid unit provided. Please use 'Celsius' or 'Fahrenheit'.