s = input()
tot_q_cnt = s.count('Q')
curr_q_cnt = 0
ans = 0
for x in s:
    if x == 'A':
    	ans += curr_q_cnt * (tot_q_cnt - curr_q_cnt)
    elif x == 'Q':
    	curr_q_cnt += 1
print(str(ans))