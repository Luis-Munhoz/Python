nome=input('qual o seu nome? ')
if nome:
    print(nome)
else:
    print('voce nao digitou nada')
print('xxxxxxxxx')
#outro metodo
print(nome or 'voce nao digitou nada') #ele para na primeira que for verdadeira
