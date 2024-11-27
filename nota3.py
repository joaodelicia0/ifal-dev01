#pegar a pontuacao do aluno 
pontuacao = int(input("Qual a pontuação:"))
#verificacao do conceito com base na pontuacao
if pontuacao >= 90:
    print("Nota: A")
elif pontuacao >= 80:
    print("Nota: B")
elif pontuacao >= 70:
    print("Nota: C")
elif pontuacao >= 60:
    print("Nota: D")
else:
    print("Nota: F")
    
#exibir ao usuario o conceito obtido

