h = int(input().split()[1])
h_s = input().split()
print(sum([(int(int(i)>h) + 1) for i in h_s]))
