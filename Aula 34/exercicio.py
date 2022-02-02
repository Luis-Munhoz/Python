while True:
    x=input("Insira um valor: ")
    y=input("Insira outro valor: ")
    op=input("Insira o operador (+ -  * /: ")
    z=input("Se você deseja encerrar digite 'sair' se não pressione qualquer tecla: ")
    if not x.isnumeric() or not y.isnumeric():
        print("Você inseriu um valor inválido")
        break
    x=float(x)
    y=float(y)
    if z=='sair':
        print("Processo encerrado")
        break
    if op=="+":
        print(f"{x} + {y} = {x+y}")
    elif op=="-":
        print(f"{x} - {y} = {x - y}")
    elif op=="*":
        print(f"{x} * {y} = {x * y}")
    elif op=="/":
        print(f"{x} / {y} = {x / y}")
    else:
        print("Operador invalido")