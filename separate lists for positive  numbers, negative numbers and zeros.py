# Initialize empty lists
numbers = []
positive = []
negative = []
zeros = []

# Accept 10 numbers from the user
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Separate the numbers into respective lists
for num in numbers:
    if num > 0:
        positive.append(num)
    elif num < 0:
        negative.append(num)
    else:
        zeros.append(num)

# Display all lists
print("\nOriginal list:", numbers)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zeros)
