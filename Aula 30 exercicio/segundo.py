nome=input('insira seu nome: ')
a=len(nome)
if a<4:
    print('nome curto')
elif a>4 and a<8:
    print('nome medio')
elif a>8:
    print('nome gigante')