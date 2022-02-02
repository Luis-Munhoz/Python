l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2 #concatenação, não soma
print(l3)
l1.extend(l2)
print(l1)
l1.insert(3,'banana') #insere na terceira case
print(l1)
l1.pop()
print(l1)
print(l3)
del(l3[1::3])
print(l3)

print(max(l3)) #maximo
print(min(l3)) #minimo

l4=list(range(0,10,2))
print(l4)
l4=range(0,10,2)
print(l4)