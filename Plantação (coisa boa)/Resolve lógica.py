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


"""Função que checa se os parêntesis estão balanceados e retorna os pares de parêntesis"""
def encontra_parens(formula):
    tabela = {} # Dicionario q retorna os pares
    stack_indices = [] # Guarda temporariamente o índice de cada

    for i, c in enumerate(formula):
        if c == '(':
            stack_indices.append(i)
        elif c == ')':
            if len(stack_indices) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            tabela[stack_indices.pop()] = i

    if len(stack_indices) > 0:
        raise IndexError("No matching opening parens at: " + str(stack_indices.pop()))

    return tabela

def get_key(my_dict, val):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    raise IndexError("Key doesn't exist")

def separa_formula(formula: str) -> list:

    # Pega o index do primeiro e último parêntesis da formula
    index_abre = formula.find("(")
    index_fecha = formula.rfind(")")
# - - - - - - - - - - - - LOGICA DO RETORNO - - - - - - - - - - - - - #

    # Teste:
    #   Se o valor - 1 (anda 1 casas para frente) é ∃ ou ∀
    #   Caso verdade:
    #       retornar o tipo, o operador, a formula e o sinal (verdadeiro/falso).
    if (
        
        (formula[index_abre + 1] == "∀" or formula[index_abre + 1] == "∃") and
        formula[index_abre + 3] == "(" 
        
        ):
        # Saída:
        return {"operador": formula[index_abre + 1:index_abre + 3], "sinal": formula[0], "formula": formula[index_abre + 3:-2]}

    # Caso falso:
    #   retornar o tipo, a primeira parte da formula, o operador,
    #   a segunda parte da formula e o sinal.
    else:
        tabela_parentesis = encontra_parens(formula)
        index_abre_1 = min(tabela_parentesis.keys())
        index_fecha_2 = max(tabela_parentesis.values())

        index_fecha_1 = tabela_parentesis[index_abre_1]
        index_abre_2 = get_key(tabela_parentesis, index_fecha_2)

        print(index_abre_1, index_fecha_1, index_abre_2, index_fecha_2)
        print(tabela_parentesis)

        
# - - - - - - - - - - - - LOGICA DO RETORNO - - - - - - - - - - - - - #

def main():

    txt = "F(∃y(∀xP(x)→P(y)))"
    txt2 = "F(∀x(P(x)∧Q(x))→(∀xP(x)∧∀xQ(x)))"
    txt3 = "F(P(a)∧Q(a))→(∀xP(x)∧∀xQ(x))"

    separa_formula(txt3)

if __name__ == '__main__':
    main()
    
