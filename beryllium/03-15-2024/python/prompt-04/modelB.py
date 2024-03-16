def convert_temperature(temperature, unit):
    if unit not in ["Celsius", "Fahrenheit"]:
        return "Invalid unit provided. Please use 'Celsius' or 'Fahrenheit'."

    if unit == "Celsius":
        converted_temperature = (temperature * 9/5) + 32
    else:
        converted_temperature = (temperature - 32) * 5/9

    return f"{round(converted_temperature, 2)} {unit}"


# Example usage:
print(convert_temperature(20, "Celsius"))  # Output: 68.00 Fahrenheit
print(convert_temperature(68, "Fahrenheit"))  # Output: 20.00 Celsius
# Output: Invalid unit provided. Please use 'Celsius' or 'Fahrenheit'.
print(convert_temperature(30, "Kelvin"))
