string='o Brasil é Pentacampeão'
lista1=string.split(' ')
print(lista1)

#usando o join
string2=' '.join(lista1) #cria uma string da lista
print(string2)

for indice,real in enumerate(lista1):
    print(indice, real, lista1[indice])


lista=[
    [0,'is'],
    [1,'lu'],
    [2,'ca']
]

print(lista)
for indice, v in lista:
    print(indice,"-", v[0], v[1])

for indice , nome in enumerate(lista): #desempacoto os valores
    print(indice,nome)

lista3='luis', 'luiz', 'luís'
n1, n2, n3 = lista3
print(n1)
print(n2)
print(n3)