# Pedra papel e tesoura

import random as r


def resultado(usr, comp):
    if usr == comp:
        return "Empate!"
    elif (usr == 1 and comp == 2) or (usr == 2 and comp == 3) or (usr == 3 and comp == 1):
        return "Computador ganhou!"
    elif (comp == 1 and usr == 2) or (comp == 2 and usr == 3) or (comp == 3 and usr == 1):
        return "Você ganhou!"
    else:
        return "Jogo inválido"


def jogada(n):
    if n == 1:
        txt = "pedra"
    elif n == 2:
        txt = "papel"
    elif n == 3:
        txt = "tesoura"
    else:
        txt = "inválido"
    return txt


# PRINCIPAL
usr = int(input("Entre com sua escolha 1 (pedra), 2 (papel) ou 3 (tesoura):"))
comp = r.randint(1, 3)
txtusr = jogada(usr)
txtcomp = jogada(comp)


# OUTPUT
print("Escolha do computador: %i" % comp)
print("Escolha do usuário: %s" % txtusr)
print("Escolha do computador: %s" % txtcomp)
print(resultado(usr, comp))
