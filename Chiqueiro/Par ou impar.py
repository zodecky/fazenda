"""
Esse é o código de um jogo de par ou ímpar,
em que o computador sempre joga par e o usuário ímpar.
O jogador da a entrada de um número por meio do teclado
(de 1 a 10, simulando o jogo real) e o computador gera
um número aleatório (também de 1 a 10).

O resultado final é dado após 10 partidas
"""

# Indica que a biblioteca padrao random será incluída (não precisa ser baixada)
# (usada para gerar números aleatórios)
import random as r

# Define as variáveis de pontuação (placar 0 X 0)
scoreComp = 0
scorePlayer = 0

# Quantas vezes a partida será jogada
# (quantas vezes o loop do jogo roda, no caso, 10)
for i in range(10):

    # Define um valor aleatório de entrada para o número de jogadas
    # Será substituido na função input() pelo valor digitado pelo usuário
    nJog = 201  # número do jogador

    # Caso o número não esteja entre 1 e 10,
    # a função pede para o jogador dar outra entrada
    while (nJog > 10 or nJog < 0):
        nJog = int(input("Número entre 0 e 10: "))  # Recebe a entrada

    # Número aleatório gerado entre 1 e 10 pelo computador
    # Utiliza a biblioteca random
    nComp = r.randint(0, 10)
    print("Computador jogou %i" % (nComp))  # Escreve na tela o número selecionado pelo computador

    # Soma os números jogados pelo computador e jogador
    nTot = nJog + nComp

    # Testa se o resto da divisão da soma por 2 é 0.
    # Ou seja, se é par ou ímpar
    if nTot % 2 == 0:
        scoreComp += 1
    else:  # se não
        scorePlayer += 1
    print(("Jogo %i\nPlacar: %i x %i") % (i, scorePlayer, scoreComp))
# Fim do loop

# Ao final do jogo, determinar vencedor:
if scorePlayer > scoreComp:
    print("Voce venceu")
elif scorePlayer < scoreComp:
    print("Computador venceu")
elif scorePlayer == scoreComp:
    print("Empate")
