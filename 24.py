# Declarando variáveis
n:int = 0    

# Início
def VerificarDiv():
    global n

    if n % 2 == 0 and n % 3 == 0:
        print("O número é divisível por 2 e 3")
    else:
        print("O número não é divisível por 2 e 3")


def main():
    global n

    n = int(input("Digite um número: "))

    VerificarDiv()

if __name__ == "__main__":
    main()
# Fim