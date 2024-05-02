# 20. Write a Python function to convert temperature from Celsius to Fahrenheit and vice versa.
def convert_temperature(temperature, from_scale, to_scale):
    if from_scale == "C" and to_scale == "F":
        return (temperature * 9/5) + 32
    elif from_scale == "F" and to_scale == "C":
        return (temperature - 32) * 5/9
    else:
        return "Invalid scale. Please use 'Celsius' or 'Fahrenheit'."

# Example usage:
print(convert_temperature(43, "C", "F"))
print(convert_temperature(68, "F", "C"))

'''
109.4
20.0
'''