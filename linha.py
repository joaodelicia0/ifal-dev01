def main():
    tamanho = int(input("Qual o tamanho da linha?"))
    gerar_linha(tamanho)
    
def gerar_linha(tamanho):
    print("{?}" * tamanho)

main()