szo = int(input('Kérem adjon meg egy szavat! '))
szo2 =int(input('Kérem adjon meg egy másik szavat! '))
szo_van = szo.find('e')
szo2_van = szo2.find('e')

szo_van = szo(szo[0])
if szo_van > 0 and szo2_van > 0:
    print('oké')
else:
    print('nem jó')