#pegar a pontuacao do aluno 
pontuacao = int(input("Qual a pontuação:"))
#verificacao do conceito com base na pontuacao
if pontuacao >= 90 and pontuacao <= 100:
    print("Nota: A")
elif pontuacao >= 80 and pontuacao < 90:
    print("Nota: B")
elif pontuacao >= 70 and pontuacao < 80:
    print("Nota: C")
elif pontuacao >= 60 and pontuacao < 70:
    print("Nota: D")
else:
    print("Nota: F")
    
#exibir ao usuario o conceito obtido

