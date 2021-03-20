a, b, c = list(map(float, input().split()))
if(a+b> c and a+c>b and b+c>a):
    print("Perimetro = {}".format(a+b+c))
else:
    print("Area = {}".format(((a+b)*c)/2))