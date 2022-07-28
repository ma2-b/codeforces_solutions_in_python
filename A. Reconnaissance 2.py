N = int(input())
heights = input().split()
for h in range(0, len(heights)): 
    heights[h] = int(heights[h])
diffs = []
for h in range(0, len(heights)-1):
    diff = heights[h] - heights[h+1]
    if diff < 0: diff *= -1
    diffs.append(diff)
    
extra_diff = heights[0] - heights[-1]
if extra_diff < 0: extra_diff *= -1
diffs.append(extra_diff)
minimal_position = diffs.index(min(diffs))
if minimal_position+1 == len(diffs):
    minimal_pair = [minimal_position + 1, 1]
else:
    minimal_pair = [minimal_position + 1, minimal_position + 2]
print(minimal_pair[0], minimal_pair[1])