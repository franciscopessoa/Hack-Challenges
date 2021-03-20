while True:
    m = int(input())
    if (m == 0):
        break
    
    touchs   = 0
    position = 1

    for i in range(m):
        track = list(map(int, input().split()))
        if track[position] == 0:
            continue
        else:
            if(position == 0):
                if(track[position+1] == 0):
                    position += 1
                    touchs += 1
                else:
                    position += 2
                    touchs += 2
            elif(position == 1):
                if(track[position+1] == 0):
                    position += 1
                    touchs += 1
                else:
                    position -= 1
                    touchs += 1
            else:
                if(track[position-1] == 0):
                    position -= 1
                    touchs += 1
                else:
                    position -= 2
                    touchs += 2
    print(touchs)