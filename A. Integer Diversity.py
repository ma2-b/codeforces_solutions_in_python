t = int(input())
for k in range(t):
    n = int(input())
    data = input().split()
    totalSum = 0
    if n == len(data):
        box = []
        for i in range(n):
            given = int(data[i])
            if given not in box:
                box.append(given)
                totalSum += 1
            else:
                newone = given * (-1)
                if newone not in box:
                    box.append(newone)
                    totalSum += 1
    print(totalSum)