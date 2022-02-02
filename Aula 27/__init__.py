usuario= input('Usuário: ')
senha= input('Senha: ')
qtd=len(usuario)
print(usuario, qtd, type(usuario), type(qtd))
if qtd<= 6:
    print("insira mais caracteres")
else:
    print('cadastrado')
    print(f'sua combinação tem mais de {len(usuario)+len(senha)} caracteres')