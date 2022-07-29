t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    l = 1
    r = n - 1
    moves = 1
    alice = a[0]
    bob = 0
    last = a[0]
    while l <= r:
        s = 0
        if moves % 2 == 1:
            while s <= last and l <= r:
                s += a[r]
                bob += a[r]
                r -= 1
        else:
            while s <= last and l <= r:
                s += a[l]
                alice += a[l]
                l += 1
        moves += 1
        last = s
    print(moves, alice, bob)