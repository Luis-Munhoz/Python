'''
Editando o print de numeros
:s - sting
:d - int
:f - float
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s,d ou f)

> - esquerda
< - direita
^ - centro
'''
num_1=10.
num_2=3.
d=num_1/num_2
print('{:.2f}'.format(d)) #ambos funcionam
print(f'{d:.2f}')
num_1=1
print(f'{num_1:0>10}') #10 zeros a esquerda de num_1
print(f'{num_1:0^10}') #10 zeros antes 5 e depois 5 de num_1
print(f'{num_1:0<10}') #10 zeros a direita de num_1
print(f'{num_1:3.2f}') #3 casas inteiras e 2 casas decimais
nome='hehe boy'
print(len(nome))
nome_formatado='{n} {n} {n}'.format(n=nome)
print(nome_formatado)
print(f'{nome:#^50}') #preenchendo