# X = 1
# Y = 2 
# Z = 3 


def game_rules(a,b):
  k = choice_points(b)
  if (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
    return 3 + k
  elif (a == 'B' and b == 'X'):
    return 0 + k
  elif (a == 'C' and b == 'X'):
    return 6 + k
  elif (a == "A" and b == "Y"):
    return 6 + k
  elif (a == "C" and b == "Y"):
    return 0 + k
  elif (a == "A" and b == "Z"):
    return 0 + k
  elif (a == "B" and b == "Z"):
    return 6 + k

def choice_points(a):
  if a == "X":
    return 1
  elif a == "Y":
    return 2
  elif a == "Z":
    return 3


with open("data.txt", "r") as rps:
  data = rps.read().split("\n")

print(data)
score_lst = []

x = len(data)
for i in range(0,x-1):
  j = data[i].split(" ")
  s = game_rules(j[0],j[1])
  score_lst.append(s)

print(score_lst)
print(sum(score_lst))
