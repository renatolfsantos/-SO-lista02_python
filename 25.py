# Declarando variáveis
h1:int = 0
m1:int = 0
h2:int = 0
m2:int = 0
t1:int = 0
t2:int = 0

# Início
def CalcTempo():
    global h1, m1, h2, m2, t1, t2

    if h2 < h1:
        t1 = (24 - h1) + h2
    else:
        t1 = h2 - h1

    if m2 < m1:
        t1 -= 1
        t2 = (60 - m1) + m2
    else:
        t2 = m2 - m1


def main():
    global h1, m1, h2, m2, t1, t2

    h1, m1 = map(int, (input("Digite o horário de início separado por espaço: ").split()))
    h2, m2 = map(int, (input("Digite o horário de término separado por espaço: ").split()))

    CalcTempo()

    print(f"A duração do jogo foi de {t1} horas e {t2} minutos")

if __name__ == "__main__":
    main()
# Fim