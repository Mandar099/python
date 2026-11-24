def even_sum(n):
    s = 0
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            s += d
        n //= 10
    return s

n = int(input("Enter number: "))
print("Sum of even digits:", even_sum(n))
