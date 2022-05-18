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

    # Pega o index do primeiro e último parêntesis da formula
    index_abre = formula.find("(")
    index_fecha = formula.rfind(")")
# - - - - - - - - - - - - LOGICA DO RETORNO - - - - - - - - - - - - - #

    # Teste:
    #   Se o valor - 1 (anda 1 casas para frente) é ∃ ou ∀
    #   Caso verdade:
    #       retornar o tipo, o operador, a formula e o sinal (verdadeiro/falso).
    if formula[index_abre + 1] == "∀" or formula[index_abre + 1] == "∃":
        return {"operador": formula[index_abre + 1:index_abre + 3], "sinal": formula[0], "formula": formula[index_abre + 3:-2]}

    # Caso falso:
    #   retornar o tipo, a primeira parte da formula, o operador,
    #   a segunda parte da formula e o sinal.
    else:
        pass

        
# - - - - - - - - - - - - LOGICA DO RETORNO - - - - - - - - - - - - - #

    print(f"Entrada: {index_abre}, Saída: {index_fecha}")


def main():
    txt = "F(∃y(∀xP(x)→P(y)))"
    txt2 = "F(∀x(P(x)∧Q(x))→(∀xP(x)∧∀xQ(x)))"
    txt3 = "F(P(a)∧Q(a))→(∀xP(x)∧∀xQ(x))"

    print(separa_formula(txt))


if __name__ == '__main__':
    main()
