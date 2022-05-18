import random

vetor_1 = [random.randint(0, 30) for _ in range(10)]
vetor_2 = [random.randint(0, 30) for _ in range(10)]

# - - - - - - - exercicio 1 - - - - - - -

soma = [vetor_1[i] + vetor_2[i] for i in range(len(vetor_1))]

print(f"\nExercicio 1:\nVetor 1: {vetor_1}\nVetor 2: {vetor_2}")
print(f"Soma vetorial: {soma}\n")

# - - - - - - - exercicio 2 - - - - - - -

escalar = random.randint(0, 5)
mult = [escalar * vetor_1[i] for i in range(len(vetor_1))]

print(f"\nExercicio 2:\nVetor: {vetor_1}, Escalar: {escalar}\nMulti: {mult}")

# - - - - - - - exercicio 3 - - - - - - -

matriz = []
linha = []
for e in range(10):
    for i in range(10):
        linha.append(vetor_1[e] * vetor_2[i])
    matriz += [linha]
print(matriz)
