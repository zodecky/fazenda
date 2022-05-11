palavra_secreta = input("Entre com a palavra secreta: ")

def retornaPalavra(txt, lista):
    if txt == "":
        return ""
    if txt[0] in lista:
        return txt[0] + retornaPalavra(txt[1:], lista)
    return "_ " + retornaPalavra(txt[1:], lista)
    
def tem_todas_as_letras(palavra_secreta, lista):
    if palavra_secreta == "":
        return True
    if palavra_secreta[0] in lista:
        return True and tem_todas_as_letras(palavra_secreta[1:], lista)
    else:
        return False
    
#Principal

tentativas = 2 * len(palavra_secreta)
erro = 0
letra = ""
lista = ""

while True: #loop principal do jogo
    print("TENTATIVAS RESTANTES: %i"%tentativas)
    while len(letra) != 1:
        letra = input("Entre com uma letra: ") #entrada
    
    if letra in palavra_secreta:
        lista += letra
        print("CERTO!")
    else:
        print("ERRADO! -1 tentativa")
        tentativas -= 1 #remove tentativa
        erro += 1
        print("%i Erro(s)"%erro)
        
    
    letra = ""    
    palavra_retornada = retornaPalavra(palavra_secreta, lista)
    print("Palavra:\n%s"%(palavra_retornada))
    
    if tem_todas_as_letras(palavra_secreta, lista):
        print("Você venceu!")
        break
    elif tentativas < 1:
        print("ENFORCADO!!")
        break