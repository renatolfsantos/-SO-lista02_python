import math

# Declarando variáveis
a:float = 0
b:float = 0
c:float = 0
x1:float = 0
x2:float = 0
delta:float = 0

# Início
def CalcDelta():
    global a, b, c, delta
    delta = (b * b) - (4 * a * c)

def CalcRaiz():
    global a, b, delta, x1, x2

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

def main():
    global a, b, c, x1, x2, delta

    a = float(input("Digite o valor do coeficiente A: "))
    b = float(input("Digite o valor do coeficiente B: "))
    c = float(input("Digite o valor do coeficiente C: "))

    CalcDelta()
    if delta < 0:
        print("Não há soluções reais para a equação") 
    else:
        CalcRaiz()
        if delta == 0:
            print(f"A raiz da equação é: {x1}")
        else:
            print(f"As raízes da equação são: {x1} e {x2}")

if __name__ == "__main__":
    main()
# Fim