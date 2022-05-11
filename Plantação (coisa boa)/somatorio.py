import math

a0 = 1
a1 = 21
soma = a0

while a0 < a1:
    a0 += 2
    soma += a0

print(soma)

n = 0
r = 1
res = 0
while res != math.pi:

    if n%2 == 0:    
        res += 4/r
    elif n%2 == 1:
        res -= 4/r
    r += 2

    n += 1
    print(res)
print(n)
