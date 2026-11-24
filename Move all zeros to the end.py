a = list(map(int, input("Enter numbers: ").split()))

b = [x for x in a if x != 0]
b += [0] * a.count(0)

print("Final list:", b)
