t = int(input())

for i in range(1, t+1):
    l, r = list(map(int, input().split()))
    borings  = 0
    boringsT = 0
    for x in range(l, r+1):
        count   = 1
        for y in str(x):
            if(int(y)%2 == count%2):
                borings+=1
            count += 1
        if(borings == len(str(x))):
            boringsT += 1
        borings = 0
    print("Case #{}: {}".format(i, boringsT))