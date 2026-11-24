a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

c = [x for x in a if x in b]

print("Common elements:", list(set(c)))