def solution(coins):
    group1=0
    group2=0
    result_group=0
    coins=sorted(coins)
    for i in coins:
        group1+=i
    for i in coins[::-1]:
        group2+=i
        result_group+=1
        if group2>(group1/2):
            break
    return result_group
if __name__ == "__main__":
    coins = input()
    coins_price = list(map(int,input().split()))
    print(solution(coins_price))