a=input("Insira um numero inteiro: ")
if a.isdigit():
    a=int(a)
    b=a%2
    if b==0:
        print(a, 'é par')
    else:
        print(a, 'é impar')
else:
    print('não é numero inteiro')
