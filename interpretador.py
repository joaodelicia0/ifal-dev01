def operação(numero1, operador, numero2):
    if operador == "+":
        print(numero1 + numero2)
    elif operador == "-":
        print(numero1 - numero2)
    elif operador == "*":
        print(numero1 * numero2)
    elif operador == "/":
        print(numero1 / numero2)
    elif operador == "%":
        print(numero1 % numero2)
    elif operador == "**":
        print(numero1 ** numero2)
    else:
        print("Operação não identificada")
    return(numero1, operador, numero2)



expressao = input("Qual sua Expressão?")

numero1, operador,numero2 = expressao.split()

numero1 = int(numero1)
numero2 = int(numero2)

operação(numero1, operador, numero2)