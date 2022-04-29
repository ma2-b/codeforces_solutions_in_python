n = int(input())
number=0
l = []
for i in range(n):
    s,e = list(map(int,input().split()))
    number+=e
    number-=s
    l.append(number)
print(max(l))