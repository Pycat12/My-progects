import re
s = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.fullmatch("A", s)
print(result)