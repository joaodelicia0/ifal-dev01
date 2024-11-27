def main():
    num = float(input("digite o numero"))
    if  par(num):
        print("o número é par")
    else:
        print("o número é impar")

    
def par(num):
    
    if num % 2 == 0:
       return True
    else:
        return False
    

main()