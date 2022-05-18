"""Programa para resolver as coisas de lógica de primeira ordem."""


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


"""Função que checa se os parêntesis estão balanceados"""


def teste_parentesis(myStr):
    stack = []
    open_list = ["{", "[", "("]
    close_list = ["}", "]", ")"]
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Parêntesis desbalanceados!"
    if len(stack) == 0:
        return "Parêntesis balanceados!"
    else:
        return "Parêntesis desbalanceados!"


def separa_formula(formula: str) -> list:
    saida = formula.find(sub[])
    print(saida)


def main():
    txt = "∃y(∀xP(x)→P(y))"
    txt2 = "∀x(P(x)∧Q(x))→(∀xP(x)∧∀xQ(x))"

    print(teste_parentesis(txt))
    separa_formula(txt)


if __name__ == '__main__':
    main()
