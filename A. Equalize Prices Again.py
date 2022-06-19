t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    suma = sum(a)
    if suma % n == 0:
        print(suma//n)
    else:
        print((suma//n)+1)