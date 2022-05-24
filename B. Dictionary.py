num_cases = int(input())
 
start_index = ord('a')
 
def berland_index(sl, el):
    if el<sl:
        return (25 * (sl - 1) + el)
    else:
        return (25 * (sl - 1) + el - 1)
 
answers = []
 
for i in range(0, num_cases):
    s = input()
    sl = ord(str(s)[0]) + 1 - start_index
    el = ord(str(s)[1]) + 1 - start_index
    answers.append(berland_index(sl,el))
 
for i in answers:
    print(i)