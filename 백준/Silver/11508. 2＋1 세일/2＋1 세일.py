from sys import stdin

n = int(input())
m = list(map(int,stdin.read().split()))
m.sort(reverse = True)
count = 0

for i in range(n):
    if(i%3!=2):
        count += m[i]
print(count)