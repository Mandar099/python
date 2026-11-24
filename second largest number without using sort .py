numbers = []

for i in range(5):
    num = float(input(f"Enter positive number {i + 1}: "))
    numbers.append(num)

# Initialize to 0 since all inputs are positive
largest = 0
second_largest = 0

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == 0:
    print("There is no second largest element (all numbers might be identical).")
else:
    print("The list is:", numbers)
    print("The second largest element is:", second_largest)



# a = list(map(int, input("Enter 5 numbers: ").split()))

# a.remove(max(a))
# print("Second largest:", max(a))