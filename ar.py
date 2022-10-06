
NÉMET = 19
BRIT = 20
CSEH = 21
LENGYEL = 23
MAGYAR = 27

netto_ar = float(input('Hogyér\' adnak egy mütyürkét? '))
print(f'A mütyürke bruttó árai: ')
print(f' {netto_ar*(1+NÉMET/100):10.2f} picula Németországban.')
print(f' {netto_ar*(1+BRIT/20100):10.2f} picula a ködösben.')
print(f' {netto_ar*(1+CSEH/100):5.2f} picula Svejk hazájában.')
print(f' {netto_ar*(1+LENGYEL/100):<10.2f} picula a másik jóbarátnál.')
print(f' {netto_ar*(1+MAGYAR/100):^10.2f} picula Magyarországon.')