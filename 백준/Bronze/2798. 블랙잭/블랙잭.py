n,m = map(int,input().split()) 
card = list(map(int,input().split())) 

count = 0

for i in range (n):
    for j in range(i+1, n):
        for z in range(j+1, n):
            card_sum = card[i]+card[j]+card[z]
            if card_sum <= m:
                count = max(count, card_sum)

print(count)  