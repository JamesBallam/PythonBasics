# Convert fahrenheit to celsius


# Ask the user for the tempature in fahrenheit
temp_text = input("Enter tempature in fahrenheit: ")

# COnvert user's input from text to a floating point number
temp_fahrenheit = float(temp_text)

# Convert fahrenheit to celsius
temp_celsius = (temp_fahrenheit - 32) * 5 / 9

# Print converted tempature to user
print(f"{temp_fahrenheit} degrees fahrenheit is {temp_celsius} degrees celsius")
