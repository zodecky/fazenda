# Gabriel Zagury de Magalhães
# 2210912

def crip(senha):
    if senha == "":
        return ""
    letra = senha[0]
    if (ord(letra) + 11) > 122:
        letra_nova = chr(32 + ord(letra) + 11 - 122)
    else:
        letra_nova = chr(11 + ord(letra))
    return letra_nova + crip(senha[1:])


def uncrip(senha):
    if senha == "":
        return ""
    letra = senha[0]
    if (ord(letra) - 11) < 32:
        letra_nova = chr(122 - (-1 * (ord(letra) - 11) + 32))
    else:
        letra_nova = chr(-11 + ord(letra))
    return letra_nova + uncrip(senha[1:])


senha = "atacarBerlimAs23horas hoje+1dia"
cript = crip(senha)
uncript = uncrip(cript)

print(senha)
print(cript)
print(uncript)
