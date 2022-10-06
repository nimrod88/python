import random

feldobások = []
for _ in range(10):
    feldobás = random.choice(['f', 'í'])
    feldobások.append(feldobás)

print('A feldobások:', ', '.join(feldobások))

fej_után_fej = 0
for index, feldobás in enumerate(feldobások):
    if index > 0 and \
        feldobás == 'f' and feldobások[index-1] == 'f':
        fej_után_fej +=1

print('Ennyiszer volt fej után fej: ', fej_után_fej)