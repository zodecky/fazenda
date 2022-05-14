import random as r

scoreComp = 0
scorePlayer = 0

for i in range(10):

    nJog = 201
    nMOD = 1

    while (nJog > 10 or nJog < 0):
        nJog = int(input("Número entre 0 e 10: "))

    nComp = r.randint(0, 10)
    print("Computador jogou %i" % (nComp))

    nTot = nJog + nComp

    if nTot % 2 == 0:
        scoreComp += 1
    else:
        scorePlayer += 1
    print(("Jogo %i\nPlacar: %i x %i") % (i, scorePlayer, scoreComp))

if scorePlayer > scoreComp:
    print("Voce venceu")
elif scorePlayer < scoreComp:
    print("Computador venceu")
elif scorePlayer == scoreComp:
    print("Empate")
