
olv = 1539 
forr = 2750

ho = int(input('Hőfok: '))
ho = float(input('Hőfok: '))

if ho < olv:
    print('Szilárd')
elif ho < forr:
    print('Folyékony')
else:
    print('Gáz')