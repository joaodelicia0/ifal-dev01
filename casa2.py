def main():
    nome = input("Qual o personagem do Harry Potter? ").title()
    person(nome)

def person(nome):
    if nome == "Harry" or nome == "Hermione" or nome == "Rony":
         print(f"Faz {nome} parte da Grfinoria")
    elif nome == "Draco":
        print(f"Faz {nome} parte da Sonserina")
    elif nome == "Luna":
        print(f"Faz {nome} parte da Cornival")
    elif nome == "Cedric":
        print(f"Faz {nome} parte da Lufa-Lufa")
    else:
        print("Personagem não encontrado")

main()