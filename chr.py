
print(chr(97))
print(chr(35))
print(chr(8364))
print(chr(8721))
print(ord('a'))
print(ord('€'))

#vnev = input("Vezetéknév: ")
#knev = input("Keresztnév: ")
#teljesnev = vnev.rstrip() + knev.rstrip()
#print(teljesnev)

szoveg = "körte"
print(len(szoveg))

szoveg2 = 'szilva'
betu = szoveg2[0]
print(betu)

szoveg3 = 'valami'
for karakter in szoveg3:
    print(karakter)

hossz=len(szoveg3)
for i in range(1, hossz):
    print(szoveg[1])

gy = 'szilva'
print(gy[2:5])
print(gy[:3])
print(gy[3:len(gy)])
print(id(gy))
gy2=gy[:]
print(id(gy2))
gy is gy2

szoveg4 = 'Kati, Lajos, Mari'
resz = szoveg4[6:]
print(resz)
resz2 = (szoveg4[6:9])
print(resz2)
resz3 = szoveg4[:9]
print(resz3)

szoveg5 = 'alma:körte:barack'
tomb = szoveg.split(':')
print(szoveg5)

dolgozo = 'Nagy János:Szolnok:3840000'
(nev, telepules, fizetes) = dolgozo.split(':')