lista = [1, 4, 5, 6, 8, 9, 26, 247]
i = 0

while True:
    try:
        lista[i] += 1
    except:
        break
    i += 1

print(lista)


lista2 = [["batata", 14], ["luisa", 89]]

print(lista2[1][0])
