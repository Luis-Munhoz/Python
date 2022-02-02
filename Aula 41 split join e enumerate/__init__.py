"""
split - dividir strings #str
join - juntar uma lista #str
enumerate - enumerar elementos iteraveis como listas
"""
frase = "o Brasil é o pais do futebol, o Brasil é pentacampeão"
lista=frase.split(' ') #estou usando o espaço para dividir se coloco ('A') divido quando tiver um A
print(lista)
print()
lista2=frase.split(',')
print(lista2)
print()
hehe=frase.split('o ') #pode usar mais de um caracter note que o "o" some
print(hehe)

print('XXXXXXXXXXXXXXXXX')
for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)} vezes na frase') # .count(X) conta quantas vezes tem X na lista

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print()
palavra=''
contagem=0
for valor in lista:
    qtd=lista.count(valor)

    if qtd>contagem:
        contagem=qtd
        palavra=valor
print('a palavra que mais apareceu é', palavra, 'e apareceu' ,contagem, "vezes")

#.strip() remove o espaço no final e no inicio
#.captalize deixa a primeira letra maiscula
