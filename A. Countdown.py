t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    operations = 0 
    for i in range(n):
        if s[i] != "0":
            operations+=1 
            operations+=int(s[i])
    if s[-1] != "0":
        operations-=1
    print(operations)