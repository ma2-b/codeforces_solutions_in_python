t = int(input())
for _ in range(t):
    s = input()
    print(min((len(s) - 1) // 2, s.count('0'), s.count('1')))