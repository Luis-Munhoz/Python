Nome='Luís Fernando Taiacol Munhoz'
idade = 19
altura=2.00
e_maior= idade>18
massa=101.97
data=True
Data=False
print('Nome:', Nome)
print('idade:', idade)
print('altura:', altura)
print('maior de idade?:', e_maior)
print(data, Data)
imc=massa/(altura**2)
print(Nome, 'tem:', idade, 'anos de idade,', 'seu imc é', imc)
print(f'{Nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #método para facilitar o print o f faz isso as variaveis
#ficam dentro do {}
#o {imc:.2f} é para o float ter só 2 casas decimais        0      1     2
print('{0} tem {1} anos de idade e seu imc é {2}'.format(Nome, idade, imc)) #igual em C, o {} é na ordem
