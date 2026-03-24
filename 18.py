# Declarando variáveis
n1:int = 0
n2:int = 0
dif:int = 0

# Início
def CalcDif():
    global n1, n2, dif

    if n1 > n2:
        dif = n1 - n2
    else:
        dif = n2 - n1


def main():
    global n1, n2
    
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))

    CalcDif()
    print(f"O resultado da diferença é: {dif}")


if __name__ == "__main__":
    main()
# Fim