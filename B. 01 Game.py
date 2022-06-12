t = int(input())
for i in range(t):
    one = 0
    zero = 0 
    s = input()
    n = len(s)
    for j in range(n):
        if s[j] == '1':
            one+=1
        else:
            zero+=1 
    turn = min(zero,one)
    if turn == 0 or turn % 2 == 0:
        print("NET")
    else:
        print("DA")