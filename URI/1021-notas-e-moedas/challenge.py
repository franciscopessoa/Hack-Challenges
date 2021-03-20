# TODO NOT COMPLETED
value = float(input())
print("NOTAS:")
for n in [100, 50, 20, 10, 5, 2]:
    rest    = value%n
    cedules = int((value - rest)/n)
    value   = rest
    print("{} nota(s) de R$ {:.2f}".format(cedules,n))
print("MOEDAS:")
print(rest)
for m in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    rest  = value%m
    coins = int((value - rest)/m)
    value = rest
    print(rest)
    print("{} moeda(s) de R$ {:.2f}".format(coins,m))
print(rest)
