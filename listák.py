ps = [10, 20, 30, 40]
qs = ["alma", "eper", "barack"]
print(ps)
print(qs)

zs = ["hello", 2.0, 5, [10, 20]]
print(zs[3])
print(zs)

szotar = ["alma", "sajt", "kutya"]
szamok = [17, 123]
ures_lista = []
print(szotar, szamok, ures_lista)

szamok = [17, 123]

print(szamok[0])
for i in enumerate(szamok):
    print(i)

for (i, ert) in enumerate(szamok):
    szamok[i] = ert**2
    print(szamok[i])

for (i, v) in enumerate(["banán", "alma", "körte", "citrom"]):
    print(i, v)

s_lista = []
s_lista.append(6)
s_lista.append(20)
s_lista.append(4)
s_lista.append(16)
print(s_lista)

s_lista.insert(1, 10)
print(s_lista)

s_lista.insert(0, 16)
print(s_lista)

print(s_lista.count(16))

s_lista.extend([5, 9, 5, 11])
print(s_lista)

print(s_lista.index(9))

s_lista.reverse()
print(s_lista)

s_lista.sort()
print(s_lista)

s_lista.remove(16)
print(s_lista)

szoveg_lista = ["barack", "alma", "mandarin"]
szoveg_lista.sort()
print(szoveg_lista)
szoveg_lista2 = ["én", "te", "ők", "mi", "ti", "ők"]
szoveg_lista2.sort()
print(szoveg_lista2)