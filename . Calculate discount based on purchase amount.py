a = float(input("Enter amount: "))

if a >= 5000:
    d = a * 20 / 100
elif a >= 3000:
    d = a * 15 / 100
elif a >= 1000:
    d = a * 10 / 100
else:
    d = 0

print("Discount:", d)
print("Total:", a - d)