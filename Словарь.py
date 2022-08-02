lib = {"Яблоко": "красное","банан": "желтый","лайм": "зеленый",}
del (lib["Яблоко"])
for k in lib.keys():
    print(k)
for m in lib.values():
    print(m)
for d in lib.items():
    print(d)
lib["банан"] = "зеный"
print(lib["банан"])