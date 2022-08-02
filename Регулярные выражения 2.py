import re
s = "Ооо да вы из англии "
result = re.findall(r"[бвгджзклмнпрстфхчшщБВГДЖЗКЛМНПРСТФХЧШЩ]\w+", s)
print(result)