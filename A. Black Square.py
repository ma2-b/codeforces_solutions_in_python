calories = list(map(int, input().split())) 
game = input()
answer = game.count('1') * calories[0] + game.count('2') * calories[1] \
      + game.count('3') * calories[2] + game.count('4') * calories[3]
print(answer)