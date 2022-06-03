t = int(input())
for i in range(t):
    a = input()
    if len(a)%2 == 1:
        print("NO")
    else:
        if a[:len(a)//2] == a[len(a)//2:]:
            print("YES")
        else:
            print("NO")