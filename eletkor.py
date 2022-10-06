
nev = input("Kérem adja meg a nevét ")
print(nev)
ÉV = 2022
udv = (f'Üdvőzőllek {nev}')
print(udv,"szép napot kívánok neked", sep = " ")
eletkor=int(input("kérem adja meg a születési évét"))
eletk = ÉV- eletkor
if eletk < 14:
    print('Általános iskola')

elif eletk > 14 | eletk < 18:
    print('Közép iskola')

elif eletk >= 18:
    print('Felnőtt')

