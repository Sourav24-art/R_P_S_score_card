
def W_D_L_condition(a,b):
  if b == "X":
    #have to lose
    if a == "A":
      return 3 
    elif a == "B":
      return 1
    elif a == "C":
      return 2
  elif b == "Y":
    score_2 = 3
    #have to draw
    if a == "A":
      return 1 + score_2
    elif a == "B":
      return 2 + score_2
    elif a == "C":
      return 3 + score_2
  elif b == "Z":
    score_3 = 6 
    #have to win 
    if a == "A":
      return 2 + score_3
    elif a == "B":
      return 3 + score_3
    elif a == "C":
      return 1 + score_3


with open("data.txt", "r") as rps:
  data = rps.read().split("\n")

print(data)
score_lst = []

x = len(data)
for i in range(0,x-1):
  j = data[i].split(" ")
  s = W_D_L_condition(j[0],j[1])
  score_lst.append(s)

print(score_lst)
print(sum(score_lst))
