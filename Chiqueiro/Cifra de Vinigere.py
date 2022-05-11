# Gabriel Zagury de Magalhães 
# 2210912

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] #define o alfabeto


#- - - - - - - - - - - - - - Função que desloca listas - - - - - - - - - - - - - - -#

def desloca(lista, deslocamento): #desloca elementos de uma lista
    lista_deslocada = [] #cria a nova lista, que vai ser a deslocada
    
    """ 
    #loop 1
    O faz um loop que roda o (tamanho da lista - deslocamento) vezes.
    a cada loop, pega o indice do loop e soma ao deslocamento (indice 0 vira 0 + deslc) e adiciona cada um ao final da nova lista. 
    
    #loop 2
    Roda (deslocamento) vezes.
    Pega o indice 0 + i e coloca no final (ate chegar no deslocamento)
    
    """     

    #loop 1
    for i in range(len(lista) - deslocamento): 
        lista_deslocada.append(lista[i + deslocamento])
        
    #loop 2    
    for i in range(deslocamento):
        lista_deslocada.append(lista[i])
        
 #Saída:       
    return lista_deslocada 
    
# - - - - - - - - - - - - - - - - Cria a tabela - - - - - - - - - - - - - - - - - -#

tabela = [alfabeto]
for i in range(25):
    tabela.append(desloca(alfabeto, i+1))
    
    
# - - - - - - - - - - - - - - - Funções da cifra - - - - - - - - - - - - - - - - -#
def repete_str(txt, tamanho):
    
    tamanho_texto = len(txt)
    quantas_vezes_cabe = tamanho // tamanho_texto
    resto = tamanho % tamanho_texto
    
    txt_repetido = ""
    for i in range(quantas_vezes_cabe):  #Repete o texto quantas vezes ele cabe inteiro
        txt_repetido += txt * (i + 1)
        
    txt_repetido += txt[0:resto] #Adiciona o que falta
    
    return txt_repetido #retorna o texto repetido
    
def crip_r(senha, chave): #Função recursiva de crip
    if senha == "": #Se a senha ou a chave forem vazias (possuem mesmo tamanho), retornar vazio
        return ""

    """
    Pega a primeira letra da chave e da senha a ser encriptada
    e transforma essa letra em um número de 0 a 26
    """

    linha = alfabeto.index(chave[0])
    coluna = alfabeto.index(senha[0])
    
    letra_nova = tabela[linha][coluna]
    
    return letra_nova + crip_r(senha[1:], chave[1:])
    
def crip(senha, chave_i):
    tamanho_senha = len(senha)
    chave = repete_str(chave_i, tamanho_senha)
    return crip_r(senha, chave)
    
print(crip("bananas", "jao"))


