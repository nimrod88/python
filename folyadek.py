# Naponta legalább 2,5 liter folyadékot kell fogyasztanunk,
# és ivásból nem vagyunk valami jók.  Írjunk programot,
# amelyik bekéri, hogy egy-egy alkalommal hány decit ittunk!
# Teszi mindezt addig, amíg 0 értéket nem adunk meg.
# Minden bekéréskor kiírja, hogy addig hány litert ittunk összesen,
# és ha elérjük a 2,5 litert, akkor erről is megemlékezik.
# 3,5 liter fölött kilép, szépen elbúcsúzva tőlünk.
'''
elso = "víz"
while elso != 0:
    elso = int(input("Hány dl vízet ittál ezzel az alkalommal? "))
    print("Eddig", elso, "liter vízet ittál")
    if elso >= 2.5 and elso < 3.5:
        print("Eleget ittál ma!")
    elif elso >= 3.5:
        print("Helló!")

össz = 0
while össz <= 35 and (ivás:=int(input('Hány decit ittál?'))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f} litert ittál.')
    if össz >= 25:
        print('Már sikerült elérned a 2,5 litert.')
print('Béka nő a hasadba!')

t=[3, 8, 2, 4, 5, 1, 6]
t1 = ['d', 'f', 'g', 'h', 'j', 'k', 'u']
osszeg = 0
szorzat = 1
konkat = ' '
for num in t:
    osszeg = osszeg + num
    szorzat = szorzat * num
    konkat = konkat + num
print("Összeg: ", osszeg)
print("Szorzat: ", szorzat)

count = 0
for num in t:
    if num > 5:
        count = count + 1
print("5-nél nagyobb: ", count)

n = len(t)
ker = 5

i = 0
while i < n and t[i] != ker:
    i = i + 1

if i<n:
    print("Van ilyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)

n = len(t)
ker = 5

i = 0
while t[i] != ker:
    i = i + 1

print("Hányadik helyen van: ", i+1)
'''
osszeg = 0
megszamol = 0
l = [2.5 ,4, 6, 7, 2, 3, 4]
for suly in l:
    osszeg = osszeg + suly
print("Összeg: ", osszeg)
if suly >= 3:
    megszamol = megszamol + 1
    print(megszamol)