# Declarando variáveis
n1:float = 0
n2:float = 0
n3:float = 0
n4:float = 0

# Início
def CalcOrdem():
    global n1, n2, n3, n4

    if n4 > n1 and n4 < n2:
        print(f"Os números em ordem crescente são: {n1}, {n4}, {n2}, {n3}")
    elif n4 > n2 and n4 < n3:
        print(f"Os números em ordem crescente são: {n1}, {n2}, {n4}, {n3}")
    elif n4 > n3:
        print(f"Os números em ordem crescente são: {n1}, {n2}, {n3}, {n4}")
    else:
        print(f"Os números em ordem crescente são: {n4}, {n1}, {n2}, {n3}")   

def main():
    global n1, n2, n3, n4

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))
    n4 = float(input("Digite o quarto número: "))

    CalcOrdem()

if __name__ == "__main__":
    main()
# Fim