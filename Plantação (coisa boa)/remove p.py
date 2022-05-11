def removeCaracter_r(p, r):
    if p == "":
        return ""
    if p[0] != r:
        return p[0] + removeCaracter_r(p[1:], r)
    else:
        return "" + removeCaracter_r(p, r)


print(removeCaracter_r("batata", "b"))
