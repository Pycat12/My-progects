import builtins
print(dir(builtins))
y = 2
def degree(x):
    return y ** x
print(degree(4))
def degree(x):
    y = 2
    return y ** x
print(degree(4))
def degree(x):
    y = 2
    def degree_two():
        return  y ** x
    return degree_two()
print(degree(4))
