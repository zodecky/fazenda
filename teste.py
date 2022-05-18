"""Função só aceita parêntesis balanceados!"""
def achaParentesis(formula):

    i = 0 # Contador de loops
    lista_index_abertura = [] # Lista com os index de abertura
    lista_index_fechamento = [] # Lista com os index de fechamento

    while formula != "":
        if formula[0] == "(":
            lista_index_abertura.append(i)
        if formula[0] == ")":
            lista_index_fechamento.append(i)
        
        formula = formula[1:] # Remove letra da formula
        i += 1 #incrementa loop

    print(lista_index_abertura, lista_index_fechamento)

achaParentesis("(P(a)∧Q(a))→(∀xP(x)∧∀xQ(x))")


def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret

print(find_parens("(P(a)∧Q(a))→(∀xP(x∧∀xQ(x))"))
