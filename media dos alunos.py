def media(nota_da_prova, media_da_turma):
    return nota_da_prova * 0.85 + media_da_turma * 0.15

def obtemNota(texto):
    nota = float(input(texto))
    while nota < 0 or nota > 10:
        print("Incorreto!")
        nota = float(input(texto))
    return nota
    

matricula = int(input("Digite a matrícula ou 0 para parar: "))

qt_media_maiorque_7 = 0
qt_media_menorque_3 = 0

soma_media = 0
qt_alunos = 0 # Quantidade de iterações

menor_media = 3333 # Número maior que o domínio

while matricula != 0:

    nota_da_prova = obtemNota("Digite a nota da prova:")
    media_da_turma = obtemNota("Digite a média dos trabalhos da turma: ")

    media = round(media(nota_da_prova, media_da_turma), 2)

    print(f"\n\nAluno de matrícula {matricula}, sua média é:\n\t{media}\n\n\n")

    # Contagem (v1): - - - - -
    if media  > 7:
        qt_media_maiorque_7 += 1

    if media < 3:
        qt_media_menorque_3 += 1

    # Média da turma: - - - - - 
    soma_media += media
    qt_alunos += 1 # Qt de iterações

    # Menor média:
    if media < menor_media:
        contagem_menor_média = 1
        menor_media = media # Atualiza a menor média
    elif media == menor_media:
        contagem_menor_média += 1

    # - - - - - - - - - - FIM DO LOOP (lógico, não de programação) - - - - - - - - -

    matricula = int(input("Digite a matrícula ou 0 para parar:"))

# Resultados da contagem

print(f"Quantitade de médias maiores que 7: {qt_media_maiorque_7}")
print(f"Quantitade de médias menores que 3: {qt_media_menorque_3}")

# Resultados da média da turma

media_geral = soma_media / qt_alunos
print(f"Media da turma: {media_geral}")






