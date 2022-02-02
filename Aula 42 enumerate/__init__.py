lista= [
    ['Luís', 'luiz', 'delmir'], #0
    ['Camile', 'késya', 'messias'],#1
    ['Camila', 'gabriel', 'rodolfinho'],#2
]
        #0          #1      #2
print(lista)
print()
x = int(input('Insira um valor: '))
y = int(input('Insira outro valor: '))
print(lista[x][y])

for v1, v2 in enumerate(lista): #permite usar a lista para um for
    print(v1,v2)

