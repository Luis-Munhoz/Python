"""
for/else em phyton
"""
var=["Luís Fernando","Camile","Isadora"]
for valor in var:
    print(valor)
    continue
    print(valor) #nao executa pq o continue faz ele voltar pro laço
print()
começa_com_C=False
for valor in var:
    if valor.lower().startswith('c'): #startswith verifica se a palavra começa com aquela letra/combinação
        print(valor, 'começa com C')
        começa_com_C=True
else:
    print('não há palavra q começa com C')
if começa_com_C:
    print('há uma palavra q começa com C')
