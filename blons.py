macacos = {
    "Macaco Atirador" : {
      "especie": "Militar", 
      "Armamento": "Rifle", 
      "Melhor Habilidade": "Impacto Moab",
      "Preço Total": "140000"
    },
    "Macaco Mago" : {
      "especie": "Mágico", 
      "Armamento": "Varinha", 
      "Melhor Habilidade": "Lança Arcana",
      "Preço Total": "130000"
    },

    "Macaco Dardo" : {
      "especie": "Primário", 
      "Armamento": "Dardo", 
      "Melhor Habilidade": "Mestre do Plasma",
      "Preço Total": "120000",
    },
    "Macaco De Gelo" : {
      "especie": "Primário", 
      "Armamento": "Canhão de Mão", 
      "Melhor Habilidade": "Lança Gelo",
      "Preço Total": "150000",
    },
    "Macaco Morteiro" : {
      "especie": "Militar", 
      "Armamento": "Morteiro", 
      "Melhor Habilidade": "incinerabloon",
      "Preço Total": "155000",
    },
    "Arma de Dardos" : {
      "especie": "Militar", 
      "Armamento": "Metralhadora de Chão", 
      "Melhor Habilidade": "Acelerador Plasmatico",
      "Preço Total": "170000",
    },
    "Alquimista" : {
      "especie": "Mágico", 
      "Armamento": "Poções", 
      "Melhor Habilidade": "De Borracha a Ouro",
      "Preço Total": "140000",
    },
    "Super Macaco" : {
      "especie": "Mágico", 
      "Armamento": "Olhos a Lazer", 
      "Melhor Habilidade": "Templo Solar",
      "Preço Total": "160000",
    },
    "Fazenda" : {
      "especie": "Suporte", 
      "Armamento": "Não Possui", 
      "Melhor Habilidade": "Central das Bananas",
      "Preço Total": "90000",
    },
    "Macaco Engenheiro" : {
      "especie": "Suporte", 
      "Armamento": "Sentinelas", 
      "Melhor Habilidade": "Armadilha XXXG",
      "Preço total": "130000",
    }
}

 

def nomes_macacos(nome):
    if nome in macacos:
        macaco = macacos[nome]
        print(f"Nome:{nome}")
        print(f"Especie:{macaco['especie']}")
        print(f"Armamento:{macaco['Armamento']}")
        print(f"Melhor Habilidade:{macaco['Melhor Habilidade']}")
        print(f"Preço total:{macaco['Preço Total']}")
    else:
        print("Macaco não encontrado")

nome_macacos = input("Qual Macaco Vocẽ Quer?").title()

nomes_macacos(nome_macacos)


        
