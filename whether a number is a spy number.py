n = int(input("Enter number: "))
t = n
s = 0
p = 1

while t > 0:
    d = t % 10
    s += d
    p *= d
    t //= 10

if s == p:
    print("Spy number")
else:
    print("Not a spy number")