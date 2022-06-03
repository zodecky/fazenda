# Exercicio de sala 4

def aprovado(G1, G2, G3):
    if (G1**2 * G2**3 * G3**5)**(1/10) >= 5.0:
        return "Aprovado"
    return "Reprovado"


# cria
with open("notas.txt", "w") as notas:
    lista_mestre = []
    with open("alunos.txt", "r") as alunos:
        for linha in alunos:
            lista_mestre.append(linha.split())

    for i in range(len(lista_mestre)):

        matricula = lista_mestre[i][0]
        G1 = float(lista_mestre[i][1])
        G2 = float(lista_mestre[i][2])
        G3 = float(lista_mestre[i][3])
        SITUACAO = aprovado(G1, G2, G3)
        notas.write(f"{matricula}, {SITUACAO}\n")
