t = int(input())
for _ in range(t):
    n = int(input())
    if 1900 <= n:
        print('Division 1')
    elif n >= 1600 and n <= 1899:
        print('Division 2')
    elif n >= 1400 and n <= 1599:
        print('Division 3')
    elif n <= 1399:
        print('Division 4')