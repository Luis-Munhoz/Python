A=input('insere um numero ai po: ')
if True: #Se verdadeiro
    print("Verdadeiro") #4 espaços ou um tab funciona como uma chave do C
    num_1=1
    num_2=4
print(num_1, num_2)
if False:
    print('num foi')
print('sem os espaço saiu dele')
if A==0:
    print('foi')
elif num_1==1:
    print('o elif é o else mais se')
elif num_2==4: #Se algum elif entrar os demais nao vao entrar mesmo que seja verdadeiro também
    print('pode por varios')
else:
    print('else')
# Nos if da vida tem os relacionais, ==, >=, <=, >, <, != retornam ou true ou false
exp= int(A)==int(num_1)
print(num_1, A)
if exp==True:
    print('vdd', exp)
else:
    print('falso' ,exp)
