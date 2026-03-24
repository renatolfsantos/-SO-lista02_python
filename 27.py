# Início
def CalcVM(voltas, percurso, tempo):
    percurso *= voltas
    percurso /= 1000

    tempo /= 60

    return percurso / tempo

def main():
    v: int = 0
    s: float = 0
    t: int = 0
    vm: float = 0

    v = int(input("Digite o número de voltas: "))
    s = float(input("Digite a extensão do circuito em metros: "))
    t = int(input("Digite o tempo de duração em minutos: "))

    vm = CalcVM(v, s, t)

    print(f"A velocidade média foi de {vm:.2f} km/h")

if __name__ == "__main__":
    main()
# Fim