import random
fovarosok = []
fovarosok = ["Bécs", "Bern", "Párizs", "London", "Budapest", "Varsó", "Prága", "Róma", "Madrid", "Helsinki", "Moszkva", "Ankara"]
fváros = None
while fváros !='':
    print('fvárosk jelenleg', ', '.join (fovarosok))
    fváros = input('Kérek egy fvárost!')
    if fváros !='':
        fovarosok.append(fváros)

n = random.randint(1-len(fovarosok)-1)

for index, főváros in enumerate(fovarosok):
    print(index,főváros)

n = int(subset)
print('A számítógép szerint ez a főváros a legszebb:', fovarosok[n])

while len(fovarosok)> 0:
    print('fovárosaink:', ', '.join(fovarosok))
    melyik = input('Melyik főváros a legszebb, válaszd ki! ')
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print('Ilyen város nincs a listába')