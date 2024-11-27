#pegar a pontuacao do aluno 
pontuacao = int(input("Qual a pontuação:"))
#verificacao do conceito com base na pontuacao
if 90 <= pontuacao <= 100:
    print("Nota: A")
elif 80 <= pontuacao < 90:
    print("Nota: B")
elif 70 <= pontuacao < 80:
    print("Nota: C")
elif 60 <= pontuacao < 70:
    print("Nota: D")
else:
    print("Nota: F")
    
#exibir ao usuario o conceito obtido

