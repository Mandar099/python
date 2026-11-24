# Accept a positive integer from the user
num = int(input("Enter a positive integer: "))

digit_sum = 0

# Extract each digit and add it to the sum
while num > 0:
    digit = num % 10        # Get the last digit
    digit_sum += digit      # Add it to the sum
    num = num // 10         # Remove the last digit

# Display the sum of digits
print("Sum of digits:", digit_sum)

# Check if the sum is even or odd
if digit_sum % 2 == 0:
    print("The sum is Even.")
else:
    print("The sum is Odd.")
