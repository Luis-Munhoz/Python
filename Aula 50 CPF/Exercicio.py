cpf='50817999809'
novo_cpf=cpf[:-2]
reverso=10
total=0
for index  in range(19):
    if index>8:
        index=index-9
    print('digito:',cpf[index],'|index:',index,'|reverso:',reverso)
    total +=int(novo_cpf[index])*reverso
    reverso-=1
    if reverso <2:
        reverso=11
        d=11- (total%11)
        if d>9:
          d=0
        total=0
        novo_cpf+=str(d)
