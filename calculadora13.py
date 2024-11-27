raio = float(input("Qual é o raio?"))

area =  f"{(3.141516 * raio * raio):_.2f}"

area = area.replace(".",",")
area = area.replace("_",".")

print(f"a área do círculo de raio {raio} é: {area}")

