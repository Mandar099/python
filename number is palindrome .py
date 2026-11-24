n = int(input("Enter number: "))
t = n
rev = 0

while t > 0:
    d = t % 10
    rev = rev * 10 + d
    t //= 10

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")