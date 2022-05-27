class Solution:
    def __init__(self):
        self.ans = []
        i = 0
        count = 1
        while i!= 1003:
            if count%3 !=0:                
                if str(count)[-1] != "3":
                    i+=1
                    self.ans.append(count)
            count+=1
    def find(self):
        t = int(input())
        for i in range(t):
            x = int(input())
            print(self.ans[x-1])
obj = Solution()
obj.find()