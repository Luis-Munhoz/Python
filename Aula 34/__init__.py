#laço while
#debugar linha por linha seleciono um laço e clico no inseto do lado do run no topo da tela
#no debug tem explorer de variaveis
i=0
while i<50:
    i=i+1 # = i+=1
    if(i==4):
        continue #dentro de um laço ele encontra a palavra continue ele pula para o proximo laço
        print("n vai executar",i)
    else:
        print(i)
    if(i==45):
        break #para o laço
print('acabou')

x=0
y=0
while x<10:
    while y<10:
        print("(",x,",",y,")")
        y+=1
    x=x+1
    y=0
