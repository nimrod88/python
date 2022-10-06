nev2 = input('Kérem adja meg a nevét! ')
automarka = input('Kérem adjon meg egy autómárkát! ')
gyarto = input('Hol készül az ' + automarka + '? ')
sebesseg = int(input('Mennyivel megy ez a(z) ' + automarka + '? '))
mondat1 = gyarto + 'vidékein keszül a ' + automarka + ',ami ' + str(sebesseg) + 'km/h-val megy.'
print(mondat1)

mondat2 = '{} vidékein keszül a  {} ,ami {} km/h-val megy.'.format(gyarto, automarka, sebesseg)
print(mondat2)

mondat3 = '{0} vidékein keszül a  {2} ,ami {1} km/h-val megy.'.format(gyarto, sebesseg, automarka)
print(mondat3)

mondat4 = '{o} vidékein keszül a  {a} ,ami {s} km/h-val megy.'.format(o=gyarto, s=sebesseg, a=automarka)
print(mondat4)

mondat5 = '{} vidékein keszül a  {a} ,ami {} km/h-val megy.'.format(gyarto, sebesseg, a=automarka)
print(mondat5)

mondat6 = f'{gyarto} vidékein keszül a  {automarka} ,ami {sebesseg} km/h-val megy.'.format(gyarto, automarka, sebesseg)
print(f'{gyarto=}, {automarka=}, {sebesseg=}')