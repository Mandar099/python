n = int(input("Enter number: "))

if n % 2 == 0 and n % 3 == 0:
    print("Both")
elif n % 2 == 0:
    print("Divisible by 2")
elif n % 3 == 0:
    print("Divisible by 3")
else:
    print("Neither")