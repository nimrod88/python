'''
Lehet e augusztus havi hóméséklet
A legnagyobb hóméséklet
A legkisebb hóméséklet
Hány alkalommal volt a hőmeséklet 31 fok felett?
mekkora volt a hómérséklet augusztus 20.-án?
mekkora volt az átlag hőmérséklet?
mekkora volt a hőingadoszás?
Fájl írás
'''
wr=open('aug.txt','a')
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

if len(aug) == 31:
    print('Lehet augusztus havi hőmérséklet.')
else:
    print('Nem lehet augusztus havi hőmérséklet')

legnagyobb = aug[0]
for elem in aug:
    if elem > legnagyobb:
        legnagyobb=elem
print('A legmagasabb hőmérséklet',legnagyobb, 'fok volt.')

legkissebb = aug[0]
for elem in aug:
    if elem < legkissebb:
        legkissebb=elem
print('A legalacsonyabb hőmérséklet',legkissebb, 'fok volt.')

hanyszor = 0
for elem in aug:
    if elem > 31:
        hanyszor += 1
print(hanyszor)

print('Augusztus 20.-án',aug[19], ' fok volt.')

print('Az átlag hőmérséklet', sum(aug) % len(aug), 'fok volt.')

wr.close