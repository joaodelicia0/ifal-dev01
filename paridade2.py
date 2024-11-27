def main():
    num = float(input("digite o numero"))
    par(num)
    
def par(num):
    
    if num % 2 == 0:
        print("o número é par")
    else:
        print("o número é impar")


main()