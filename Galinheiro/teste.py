def encontra_parens(formula):
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


print(encontra_parens("(P(a)∧Q(a))→(∀xP(x∧∀xQ(x))"))

