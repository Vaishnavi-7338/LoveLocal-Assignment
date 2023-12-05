# Define a function 'countDigitOne' that takes an integer 'n' as input
def countDigitOne(n):
    # Initialize a variable 'count' to store the count of digit 1
    count = 0
    # Initialize a variable 'factor' to represent the current place value (1s, 10s, 100s, etc.)
    factor = 1

    # Continue the loop until there are no more digits in 'n'
    while n // factor > 0:
        # Extract the current digit at the 'factor' place
        digit = (n // factor) % 10
        # Calculate the higher and lower parts of the number
        high = n // (factor * 10)
        low = n % factor

        # Check the current digit
        if digit == 0:
            # If the digit is 0, count the occurrences in the higher part
            count += high * factor
        elif digit == 1:
            # If the digit is 1, count the occurrences in both higher and lower parts
            count += high * factor + (low + 1)
        else:
            # If the digit is greater than 1, count the occurrences in the higher part
            count += (high + 1) * factor

        # Update the 'factor' for the next iteration
        factor *= 10

    # Return the final count of digit 1
    return count

# Prompt the user to enter a value for 'n'
n = int(input('Enter the value: '))

# Call the 'countDigitOne' function with the input 'n'
result = countDigitOne(n)

# Print the result
print(f"Number of digit 1 in integers up to {n}: {result}")
