lista=['Luís','Camile','Maria']
n1,n2,n3=lista
print('n1: ',n1)
print('n2: ',n2)
print('n3: ',n3)

lista2=[1,2,3,4,5,6,7,8,9,10]
n1,n2,*gambiarra,penultimo,ultimo=lista2 #o gambiarra é uma outra lista onde foi parar o restante/ *_ caguei pros dados n uso

print(" ","gambiarra: ",gambiarra)
print("penultimo: ",penultimo)
print("ultimo: ",ultimo)
