# Declarando variáveis
n1:float = 0
n2:float = 0
maior:float = 0

# Início
def main():
    global n1, n2, maior

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    CalcMaior()
    print(f"O maior valor é: {maior}")

def CalcMaior():
    global n1, n2, maior

    if n1 > n2:
        maior = n1
    else:
        maior = n2


if __name__ == "__main__":
    main()
# Fim