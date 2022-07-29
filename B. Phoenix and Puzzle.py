from math import floor, sqrt
def is_square(x):
    s = int(floor(sqrt(x)))
    return s * s == x
t = int(input())
for _ in range(t):
    n = int(input())
    print('YES' if (n % 2 == 0 and is_square(n // 2))
          or (n % 4 == 0 and is_square(n // 4)) else 'NO')