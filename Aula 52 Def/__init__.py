def função(x=10,y=5.0):
    print(x,y)
    z=x*y
    print(z)
    return(x,y,z)
    print('xxxxxxxxxxxxxxxxx') #nao é executado
#encontro return encerra a função
def função_sem_return():
    while False:
        pass

k,y,g=função()
g=função(y='string',x=72)
a=5.0
b=10
q,w,e=função(a,b)

print(g)
print(q,w,e)

x=função_sem_return()
print(x) #o none significa que nao tem valor