barack=int(input('Mennyi barack termett? '))
#ar=int(input('Mennyibe kerül egy mázsa? '))
korte=int(input('Mennyi körte termett? '))
#ar2=int(input('Mennyibe kerül egy mázsa? '))

if barack>korte:
    print('barack több')
elif barack<korte:
    print('körte tobb')
else:
    print('egyenlő')