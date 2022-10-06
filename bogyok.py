
név = input('Mi az ős neve? ')
bogyók = int(input('Hány bogyója van? '))

if bogyók < 10:
    minősítés = 'zsenge'
elif bogyók > 20:
    minősítés = 'nagy koponya'
else:
    minősítés = 'gyűjtögető'

print(f' {név} egy {minősítés}.')