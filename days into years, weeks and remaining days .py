d = int(input("Enter days: "))

y = d // 365
d = d % 365

w = d // 7
d = d % 7

print("Years:", y)
print("Weeks:", w)
print("Days:", d)