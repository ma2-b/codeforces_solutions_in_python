t = int(input())
for k in range(t):
    n = int(input())
    heroes = sorted(list(map(int, input().split())))
    if len(set(heroes)) == 1:
        print(0)
    else:
        for i, hero in enumerate(heroes):
            if hero > heroes[0]:
                print(n - i)
                break