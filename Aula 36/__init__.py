# índices
# 0,1,2,3,4, ... 33
frase= 'o rato roeu a roupa do rei de roma'
tamanho=len(frase)
print(tamanho)
cont=0
nova_string=''
while cont< tamanho:
    print("O contador é: ",cont)
    print("A letra é :     ",frase[cont])
    cont=cont+1
cont=0
while cont < tamanho:
    nova_string +=  frase[cont]
    print(frase[cont],cont)
    cont=cont+1
print(nova_string)