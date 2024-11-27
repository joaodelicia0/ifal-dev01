def main():
    tamanho = int(input("Qual o tamanho do bloco?"))
    gerar_bloco(tamanho)
    
def gerar_bloco(tamanho):
    largura = ("{}" * tamanho)
    print(f"{largura}\n"  * tamanho, end="")

main()