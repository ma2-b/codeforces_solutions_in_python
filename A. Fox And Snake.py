def main():
    n, m = map(int,input().split())
    a = '.' * (m - 1)
    b = '#'
    c = '#' * m
    for x in range(n):
        if x % 2 == 0:
            print(c)
        else:
            print(f"{a}{b}")
            a, b = b, a
main()