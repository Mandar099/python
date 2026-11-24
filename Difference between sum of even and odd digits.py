# Accept a positive integer from the user
num = int(input("Enter a positive integer: "))

even_sum = 0
odd_sum = 0

# Extract each digit and classify it as even or odd
while num > 0:
    digit = num % 10          # Get the last digit
    
    if digit % 2 == 0:
        even_sum += digit     # Add to even sum
    else:
        odd_sum += digit      # Add to odd sum
        
    num = num // 10           # Remove the last digit

# Calculate the difference
difference = abs(even_sum - odd_sum)

# Display the results
print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)
print("Difference:", difference)
