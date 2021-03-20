t = int(input())

for i in range(1, t+1):
    n, k, s    = list(map(int, input().split()))
    diffLevels = k - s
    back       = (diffLevels * 2) + k + (n - k)
    restart    = k + n
    print("Case #{}: {}".format(i, back if back < restart else restart))