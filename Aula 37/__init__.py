'''
for
range(start, stop, step) range(começo, fim, passo)
'''

texto='phyton'

for letra in texto: #em string
    print(letra)
print('')
for n, letra in enumerate(texto):
    print(n,letra)
for numero in range(0,10,1):
    print(numero)
nova=''
for letra in texto:
    if letra=='t':
        nova=nova+letra.upper()
    elif letra=='h':
        nova=nova+letra.upper()
    else:
        nova=nova+letra
    print(nova)