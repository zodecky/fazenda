def tabuada(n):
    multiplicador = 1
    while multiplicador <= 10:
        print(f"\t{multiplicador} x {n} = {multiplicador * n}")


numero = int(input("Digite o próximo número ou 0 para finalizar: "))
while numero != 0:
    print(f"Tabuada do {numero}")
    tabuada(numero)
    numero = 2
