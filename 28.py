# Início
def CalcularNP(vendas, preco):
    if vendas < 500 and preco < 30:
        return preco * 1.10
    elif 500 <= vendas < 1000 and 30 <= preco < 80:
        return preco * 1.15
    elif vendas >= 1000 and preco >= 80:
        return preco * 0.95
    else:
        return preco * 1.00 
        
def main():
    p: float = 0
    m: int = 0
    np: float = 0

    m = int(input("Digite a média mensal de vendas: "))
    p = float(input("Digite o preço atual: "))

    np = CalcularNP(m, p)
    print(f"O novo preço será: {np:.2f} reais") 

if __name__ == "__main__":
    main()
# Fim