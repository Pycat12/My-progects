def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print(maximum(25, 17))
print((lambda a, b: a if a > b else b )(25, 14))
