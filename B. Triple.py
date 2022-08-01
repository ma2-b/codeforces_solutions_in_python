t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    dict = {}
    flag = True 
    for i in a:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
            if dict[i] == 3:
                flag = False 
                print(i)
                break 
    if flag:
        print(-1)