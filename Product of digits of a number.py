n = int(input("Enter number: "))
p = 1

while n > 0:
    d = n % 10
    p *= d
    n //= 10

print("Product:", p)