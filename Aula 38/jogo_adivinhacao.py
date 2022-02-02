#!/usr/bin/env python

"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
secreto = 'perfume'
digitadas = []
chances = 3
print()
print("Bem vindo ao jogo da adivinhação, seu objetivo é adivinhar a palavra secreta. ")
print("Para isso você tem 3 vidas, e deverá chutar letras até acertar ou adivinhar a palavra.")
print()
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra) #adiciona na lista digitadas

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()#retira a letra incorreta

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
    if chances == 2:
        print("Dica: se passa no corpo")
