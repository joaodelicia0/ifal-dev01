## informe o nome do personagem do Harry Potter 
nome = input("Qual o personagem do Harry Potter? ")
## verificar e exibir qual a casa deste personagem

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
