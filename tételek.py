t=[2, 5, 6, 9, 10, 12, 4]
'''
print("eldöntés - True/False")

wr = open('H:\iras\eldöntés.txt','w')

wr.write('t=[2, 5, 6, 9, 10, 12, 4]')
n=len(t)
wr.write('n')
ker = 5
wr.write('A keresett szám:{ker}')
i=0
while i<n and t[i] != ker:
    i = i +1
if i<n:
    print("Van ilyen ", ker)
    wr.write(f'Van ilyen ', ker)
else:
    print("Nincs ilyen ",ker)
    wr.write(f'Nincs ilyen ', ker)
wr.close()
'''

print("kiválasztás")

n=len(t)
ker= 5
i=0
while t[i] != ker:
    i = i+1
print("ezen a helyen található ", i+1)

print('lineáris keresés')

print('eldöntés (van-nincs), kiválasztás tétel (hely megadás)')
n=len(t)
print(n)
ker=5
i=0
while i<n and t[i] != ker:
    i=i+1
    if(i<n):
        print(f'van {ker} elem a listában')
        print(f'Helye {i+1}')
    else:
        print(f'nincs {ker} elem a listában')

print('Szélsőértékek')
maxElem=None
maxElem=t[0]
for elem in t:
    if elem > maxElem:
        maxElem=elem
print(maxElem)

minElem=t[0]
for elem in t:
    if elem < minElem:
        minElem=elem
print(minElem)
print(f'Egyszerű számtani átlag : {(minElem + maxElem)/2}')


wr=open('H:\iras\max.txt','w')
wr.write(f't=[2, 5, 6, 9, 10, 12, 4]\n')
maxElem = t[0]
for elem in t:
    if elem >maxElem:
        maxElem = elem
print(f'{maxElem}\n')
wr.write(f'{maxElem}\n')
wr.close

wr=open('H:\iras\min.txt','w')
wr.write(f't=[2, 5, 6, 9, 10, 12, 4]\n')
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(f'{minElem}\n')
wr.write(f'{minElem}\n')
wr.close

b=[]
c=[]
d=[]
e=[]
def dupla(num):
    return num*2

for elem in t:
    b.append(dupla(elem))
    if elem%2 ==0:
        c.append(elem)
    if elem <5:
        d.append(elem)
    if elem%2 !=0:
        e.append(elem)
print(b)
print(c)

print('kiválogatás')
print(d)

n = len(t)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if(t[j]>t[j+1]):
            tmp = t[j+1]
            t[j+1]=t[j]
            t[j] = tmp
print(t)