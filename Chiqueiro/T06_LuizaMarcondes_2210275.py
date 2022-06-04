ldescartar = ["a", 'oh', 'ah', 'yeah', 'hm', 'e', 'mas', 'nem', 'contudo',
              'entretanto', 'porém', 'todavia', 'já', 'ou', 'pois', 'portanto',
              'conseguinte', 'porquanto', 'porque', 'que', 'embora', 'conforme',
              'se', 'quando', 'conquanto', 'desde', 'apenas', 'qual',
              'contra', 'entre', 'sem', 'de', 'da', 'do', 'das', 'dos',
              'para', 'pra', 'sob', 'após', 'perante', 'sobre', 'até', 'em',
              'na', 'no', 'nas', 'nos', 'num', 'dum', 'nuns', 'por', 'trás',
              'com', 'o', 'a', 'os', 'as', 'à', 'ao', 'um', 'uns', 'uma',
              'umas', "lá"]
lpalavValid = []
lfreq = []
lpalavras = []


arq = open('/Users/Gabriel/Documents/GitHub/fazenda/Chiqueiro/alvorada.txt', 'r')

for linha in arq:
    print("- - - - - - - nova linha - - - - - - -")
    linha = linha.replace(",", "")  # Troca , por espaço
    llinha = linha.split()  # Poe na lista
    for (i, el) in enumerate(llinha):
        llinha[i] = el.lower()  # Dexa cada elemento minúsculo
    for el in llinha:
        print("el", el)
        if el in ldescartar:
            print("remove", el)
            llinha.remove(el)
    for el in llinha:
        print("append", el)
        lpalavras.append(el)
        if el not in lpalavValid:
            lpalavValid.append(el)


# print(lpalavras)
# print(lpalavValid)

for el in lpalavValid:
    soma = 0
    soma = lpalavras.count(el)
    lfreq.append(soma)


# print(lfreq)
arq.close()
