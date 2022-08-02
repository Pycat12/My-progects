print(sum([i ** 3 for i in range(1, 21) if i % 5 == 0]))
print([(i, j) for i in range(1, 21) for j in range(1, 51)])
print([i ** 2 if i > 0 else i ** 3 for i in range(-10, 11) if i % 2 == 0])