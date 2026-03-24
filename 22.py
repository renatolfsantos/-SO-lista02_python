# Declarando variáveis
n1:int = 0
n2:int = 0

# Início
def CalcOrdem():
    global n1, n2

    if n1 > n2:
        print(f"Os números em ordem crescente são: {n2}, {n1}")
    else:
        print(f"Os números em ordem crescente são: {n1}, {n2}")


def main():
    global n1, n2

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    CalcOrdem()

if __name__ == "__main__":
    main()
# Fim