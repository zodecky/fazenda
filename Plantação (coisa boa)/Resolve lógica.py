"""Programa para resolver as coisas de lógica de primeira ordem"""


"""Função usada para remover espaços que o usuário pode digitar"""
def removeCaracter_r(palavra, caracter):
    if palavra == "":
        return ""
    if palavra[0] != caracter: 
        # Caso diferente do caracter: 
        # Retorna a letra (adiciona a nova string)
        return palavra[0] + removeCaracter_r(palavra[1:], caracter)
    # Caso igual:
    # Não retorna a letra (adiciona aspas)
    return removeCaracter_r(palavra[1:], caracter)

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  

txt = "∃y(∀xP(x)→P(y))"