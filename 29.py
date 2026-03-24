# Início
def CalcInvestimento(tipo, valor):
    match tipo:
        case 1:
            return valor * 1.03
        case 2:
            return valor * 1.05
        case _:
            return valor

def main():
    t:int = 0
    v:float = 0
    final:float = 0

    t = int(input("Digite o tipo de investimento: "))
    v = float(input("Digite o valor do investimento: "))

    final = CalcInvestimento(t, v)
    print(f"Após 30 dias, o valor corrigido será: R${final:.2f}")

if __name__ == "__main__":
    main()
# Fim