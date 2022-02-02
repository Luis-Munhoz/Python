'''Contadores
While e else while
'''
cont=0 #conta de forma linear
acumulador=0 #conta de forma exponencial
x=int(input("Insira um valor: "))
while cont <= 10:
    acumulador=acumulador + cont
    cont=cont+1
    if(acumulador == x):
        break #ESSE BREAK QUEBRA O WHILE
else:
    print('Executa quando o while vira falso') #Nao executa quando ocorre um break
print('continua aqui')
