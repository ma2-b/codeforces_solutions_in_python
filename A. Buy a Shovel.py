k,r = list(map(int,input().split()))
for i in range(1,11):
    if (i * k) % 10 in [0,r]:
        break
print(i)