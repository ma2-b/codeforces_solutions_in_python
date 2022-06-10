class Solution:
    def answer(self, a:int, b:int, c:int):
        maxx =  max(a, b, c)
        arr = []
        if max(c, b) < a:
            arr.append(0)
        else:
            arr.append(1+ maxx - a)
        if max(a, c) < b:
            arr.append(0)
        else:
            arr.append(1+ maxx - b)
        if max(b, a) < c:
            arr.append(0)
        else:
            arr.append(1+ maxx - c) 
        return arr
t = int(input())
for _ in range(t):
    stdin = list(map(int, input().split()))
    obj = Solution()
    print(*obj.answer(stdin[0] , stdin[1], stdin[2]))