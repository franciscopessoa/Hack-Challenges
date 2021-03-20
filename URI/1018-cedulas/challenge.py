value = int(input())
print(value)
for n in [100, 50, 20, 10, 5, 2, 1]:
    rest    = value%n
    cedules = int((value - rest)/n)
    value   = rest
    print("{} nota(s) de R$ {},00".format(cedules,n))