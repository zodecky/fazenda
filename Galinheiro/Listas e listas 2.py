l2 = [["batata", 1.4 ], ["luisa", 9.4], ["joao", 4.5], ["gabriel", 7.0]]

def media_da_turma(lista):
    
    soma = 0 #definir soma
    
    for i in lista:
        soma += i[1]
        
    return soma / len(lista)

media = media_da_turma(l2)

for i in l2:
    if i[1] > media:
        print(i[0], i[1])
