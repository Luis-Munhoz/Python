#if elif else
#and or not
#comp1 and comp2
#verdadeira e verdadeira
#comp2 or comp2
#verdadeira ou verdadeira
#comp3 and not comp3
#verdadeira e falsa
#comp4 or not comp4
#verdadeira ou falsa
A=0
B=0
if A==0 and B<0:
    print("esta dentro do if")
elif A>0 or B>0:
    print("Dentro do elif")
else:
    print("dentro do else")
A=-3
B=2
if A==0 and not B==2:
    print('dentro do if')
elif A>0 or not B>0:
    print('dentro do elif')
else:
    print('dentro do else')
    if A<0:
        print("if dentro do if")
nome='Luís'
if 'u' in nome:
    print('há u no nome')
nome= 'asta'
if 'u' not in nome:
    print('nao tem u')
#o in pode ser usado em strings e matriz nao para inteiros ou reais
#Exercicio
usuario= input("usuario: ")
senha= input('Senha: ')
usuario_bd= 'Luís'
senha_bd= "ihuu"
if senha==senha_bd and usuario==usuario_bd:
    print('voce está logado')
else:
    print('senha incorreta')