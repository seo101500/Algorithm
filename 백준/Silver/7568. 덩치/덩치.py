n = int(input())
data = []

for i in range(n):
    x, y = map(int, input().split())
    data.append((x,y))

for j in data:
    rank = 1 
    for z in data:
        if j[0] < z[0] and j[1] < z[1]:
            rank+=1 
    print(rank, end = " ")
