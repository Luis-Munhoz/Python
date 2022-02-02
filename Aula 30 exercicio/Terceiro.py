a=input('insira o horario: ')
if a.isdigit():
    a=int(a)
    if a<0 or a>24:
        print('horario invalido')
    elif a<=11:
        print('bom dia')
    elif a>=12 and a<=17:
        print('boa tarde')
    elif a>=18:
        print('boa noite')
else:
    print('não é um horario')