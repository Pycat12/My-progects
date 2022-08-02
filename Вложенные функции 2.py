def messege(x):
    def print_messege(y):
        return x, y
    return print_messege
d = messege(4)
print(d(5))
print(d(9))