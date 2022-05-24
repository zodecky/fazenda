"""Programa para resolver as coisas de lógica de primeira ordem."""


def removeCaracter_r(palavra, caracter):
    """Função usada para remover espaços que o usuário pode digitar."""
    if palavra == "":
        return ""
    if palavra[0] != caracter:
        # Caso diferente do caracter:
        # Retorna a letra (adiciona a nova string) 
        return palavra[0] + removeCaracter_r(palavra[1:], caracter)
    # Caso igual:
    # Não retorna a letra (adiciona aspas)
    return removeCaracter_r(palavra[1:], caracter)


def encontra_parens(formula):
    """Função que checa se os parêntesis estão balanceados."""
    """Retorna os pares de parêntesis."""
    tabela = {}  # Dicionario q retorna os pares
    stack_indices = []  # Guarda temporariamente o índice de cada

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


def pega_operador(operador: str) -> str:
    if operador == "→":
        return "implicação"
    if operador == "∧":
        return "e"
    if operador == "∨":
        return "ou"
    if operador == "⇔":
        return "biequivalência"
    if operador == "¬":
        return "negação"

# - - - - - - - - - - - - - FORMULAS LOGICAS - - - - - - - - - - - - - - - #


def resolve_implicacao(sinal: str, formula_1: str, formula_2: str) -> list:
    if sinal == "F":
        lista = [f"V({formula_1})", f"F({formula_2})"]
    else:
        lista = [[f"F({formula_1})"], [f"V({formula_1})", f"V({formula_2})"]]

    return lista


def resolve_e(sinal: str, formula_1: str, formula_2: str) -> list:
    if sinal == "F":
        lista = [[f"F({formula_1})"], [f"F({formula_2})"]]
    else:
        lista = [f"V({formula_1})", f"V({formula_2})"]
    return lista


def resolve_ou(sinal: str, formula_1: str, formula_2: str) -> list:
    if sinal == "F":
        lista = [f"F({formula_1})", f"F({formula_2})"]
    else:
        lista = [[f"V({formula_1})"], [f"V({formula_2})"]]
    return lista


def resolve_bi_implicacao(sinal: str, formula_1: str, formula_2: str) -> list:
    if sinal == "F":
        lista = [[f"V({formula_1})", f"F({formula_2})"], [f"F({formula_1})", f"V({formula_2})"]]
    else:
        lista = [[f"V({formula_1})", f"V({formula_2})"], [f"F({formula_1})", f"F({formula_2})"]]
    return lista

# - - - - - - - - - - - - - FORMULAS LOGICAS - - - - - - - - - - - - - - - #


def separa_formula(formula: str) -> dict:

    # Pega o index do primeiro e último parêntesis da formula
    index_abre = formula.find("(")
    index_fecha = formula.rfind(")")
    # - - - - - - - - - - - - LOGICA DO RETORNO - - - - - - - - - - - - - #

    # Teste:
    #   Se o valor - 1 (anda 1 casas para frente) é ∃ ou ∀
    #   Caso verdade:
    #       retornar o tipo, o operador, a formula e o sinal (verdadeiro/falso).
    if (

        # Testa se é o caso de ser uma substituição de letra
        (formula[index_abre + 1] == "∀" or formula[index_abre + 1] == "∃") and
        formula[index_abre + 3] == "("

    ):
        # Saída:
        operador = formula[index_abre + 1:index_abre + 3]
        return {"tipo": "substituicao", "operador": operador, "sinal": formula[0], "formula": formula[index_abre + 3:-2]}

    # Caso falso:
    #   retornar o tipo, a primeira parte da formula, o operador,
    #   a segunda parte da formula e o sinal.
    else:
        # Usa a função encontra_parens() para encontrar os pares de parêntesis da formula
        tabela_parentesis = encontra_parens(formula)
        # Pega o primeiro parêntesis aberto
        index_abre_1 = min(tabela_parentesis.keys())
        # Pega o último parêntesis fechado
        index_fecha_2 = max(tabela_parentesis.values())

        # Pega os respectivos pares
        index_fecha_1 = tabela_parentesis[index_abre_1]
        index_abre_2 = get_key(tabela_parentesis, index_fecha_2)

        # Saída:
        operador = formula[index_fecha_1 + 1]
        formula_1 = formula[index_abre_1 + 1:index_fecha_1]
        formula_2 = formula[index_abre_2 + 1:index_fecha_2]

        # Separa a formula nas partes que serão passadas para a próxima função
        return {"tipo": "resolucao", "operador": operador, "sinal": formula[0], "formula_1": formula_1, "formula_2": formula_2}

    # - - - - - - - - - - - - LOGICA DO RETORNO - - - - - - - - - - - - - #


def resolve_formula(dicionario: dict) -> str:
    sinal = dicionario["sinal"]
    operador = dicionario["operador"]
    tipo = dicionario["tipo"]

    if tipo == "resolucao":
        formula_1 = dicionario["formula_1"]
        formula_2 = dicionario["formula_2"]

        tipo_da_resolucao = pega_operador(operador)

        if tipo_da_resolucao == "implicação":
            return resolve_implicacao(sinal, formula_1, formula_2)
        if tipo_da_resolucao == "e":
            return resolve_e(sinal, formula_1, formula_2)
        if tipo_da_resolucao == "ou":
            return resolve_ou(sinal, formula_1, formula_2)

        print(tipo_da_resolucao)

    else:
        formula = dicionario["formula"]


def main():

    txt = "F(∃y(∀xP(x)→P(y)))"
    txt2 = "F(∀x(P(x)∧Q(x))→(∀xP(x)∧∀xQ(x)))"
    txt3 = "F(P(a)∧Q(a))→(∀xP(x)∧∀xQ(x))"
    txt4 = "V(P(a)∧Q(a))→(∀xP(x)∧∀xQ(x))"
    txt5 = "F(P(a)∨Q(a))→(∀xP(x)∨∀xQ(x))"

    formula_separada = separa_formula(txt)
    print(formula_separada)
    formula_resolvida = resolve_formula(formula_separada)
    print(formula_resolvida)


if __name__ == '__main__':
    main()
