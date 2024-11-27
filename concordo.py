def main():
    resposta = input("Você concorda?").lower()
    concordo(resposta)

def concordo(resposta):
    if resposta == "sim" or resposta == "s":
        print("Concordo")
    elif  resposta == "nao" or resposta == "n" or resposta == "não":
        print("Não concordo")

main()