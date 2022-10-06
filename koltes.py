kedd = int(input('Hány forintot költöttél kedden? '))
szerda = int(input('Hány forintot költöttél szerdán? '))
if kedd > szerda:
    print('Kedden költöttél többet,',kedd,'Ft-ot.')
elif kedd < szerda:
    print('Szerdán költöttél többet,',szerda,'Ft-ot.')
else:
    print('Kedden és szerdán is ugyanannyit költöttél.')