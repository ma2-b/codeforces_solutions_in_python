t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    all_ab = a + b
    for i in range(len(a)+len(b)):
        if all_ab[i] in a and all_ab[i] in b:
            print("YES")
            print(1,all_ab[i]) 
            break
    else:
        print("NO")