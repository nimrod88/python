wr=open('ev.txt', 'a')
wr.write('')
ev = [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305]
'''
ev=False

if len(ev) == 12:
    ev=True
    print(F'Ez egy év adatsora')
else:
    print(f'ez nem egy év adatsora')
'''
legnagyobb = ev[0]
for elem in ev:
    if elem > legnagyobb:
        legnagyobb=elem
print(legnagyobb)

legkissebb = ev[0]
for elem in ev:
    if elem < legkissebb:
        legkissebb=elem
print(legkissebb)

szamlalo = 0
for elem in ev:
    szamlalo=szamlalo+1
print(szamlalo)

hanyszor = 0
for elem in ev:
    if elem > -2400:
        hanyszor += 1
print(hanyszor)

hossz = len(ev)
ker = legnagyobb
i = 0
while ev[i] != ker:
    i += 1
print(f'legnagyobb helye: {i+1}')

hossz = len(ev)
ker = legkissebb
i = 0
while ev[i] != ker:
    i += 1
print (f'legkisebb helye: {i+1}')