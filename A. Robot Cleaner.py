import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  # decode().strip() if str
output = sys.stdout.write
  
def solve(R, C, r1, c1, r2, c2):
    if r1 == r2 or c1 == c2: return 0
 
    res = 0
    dr = dc = 1
    while True:
        if not 1 <= r1+dr <= R: dr = -dr
        if not 1 <= c1+dc <= C: dc = -dc
        res += 1
        r1 += dr
        c1 += dc
        if r1 == r2 or c1 == c2: break
    return res
 
 
 
def main():
    T = int(input())
    for _ in range(T):
        R, C, r1, c1, r2, c2 = list(map(int, input().split()))
        out = solve(R, C, r1, c1, r2, c2)
        output(f'{out}\n')
 
 
if __name__ == '__main__':
    main()