## informe o nome do personagem do Harry Potter 
nome = input("Qual o personagem do Harry Potter? ")
## verificar e exibir qual a casa deste personagem
match nome:
     case "Harry" |"Hermione" |"Rony":
        print(f"Faz {nome} parte da Grfinoria")
     case "Draca":
        print(f"Faz {nome} parte da Sonserina")
     case "Luna":
        print(f"Faz {nome} parte da Cornival")
     case "Cedric":
        print(f"Faz {nome} parte da Lufa-Lufa")
     case _:
        print("Personagem não encontrado")
