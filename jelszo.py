
bejutott = False

while not bejutott:
    felhasznalonev = input('Kérem adja meg a felhasználónevét ')
    jelszo = input('Kérem adja meg a jelszavát ')
    if felhasznalonev == 'bori99' and jelszo == 'kismehe<3':
        print('A belépés megengedve')
        bejutott = True
    else:
        print('Belépés megtagadva')