def main():
    tamanho = int(input("Qual o tamanho da coluna?"))
    gerar_coluna(tamanho)


def gerar_coluna(tamanho):
    print("[]\n" * tamanho, end="")

main()