n = int(input())
p = list(map(int,input().split()))
p.sort()
count = 0

for i in range(1,n+1):
    count+=sum(p[:i])

print(count)