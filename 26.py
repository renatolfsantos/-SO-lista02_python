# Declarando variáveis
n1:int = 0
n2:int = 0

# Início
def VerificarMult():
    global n1, n2

    if n1 > n2:
        if n1 % n2 == 0:
            print(f"{n1} é um múltiplo de {n2}")
        else:
            print(f"{n1} não é um múltiplo de {n2}")
    else:
        if n2 % n1 == 0:
            print(f"{n2} é um múltiplo de {n1}")
        else:
            print(f"{n2} não é um múltiplo de {n1}")


def main():
    global n1, n2

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    VerificarMult()

if __name__ == "__main__":
    main()
# Fim