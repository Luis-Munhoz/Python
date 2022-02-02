logged_user=False

if logged_user:
    msg='usuário logado'
else:
    msg='usuário deslogado'
print(msg)

#outro método
logged_user=False
msg='Usuário logado.' if (logged_user==True) else 'Usuário deslogado'
print(msg)

idade=19
eh= (idade>=18) #booleana
msg='pode acessar' if(eh) else 'nao pode acessar'

print(msg)