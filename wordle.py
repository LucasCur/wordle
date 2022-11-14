import os, random as r, json

format = """            ┏━━━━━━━━┓
            ┃ WORDLE ┃
            ┗━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   ┏━━━┓
┃ ✘ = Incorrect Letter & Placement ┃   ┃ # ┃
┃ ! = Correct Letter & Wrong Place ┃   ┣━━━┫
┃ ✔ = Correct Letter & Placement   ┃   ┃ # ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┣━━━┫  ┏━━━━━━━┓
                                       ┃ # ┃  ┃ TRIES ┃
 ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓     ┣━━━┫  ┗━━━━━━━┛
 ┃ ? ┃  ┃ ? ┃  ┃ ? ┃  ┃ ? ┃  ┃ ? ┃     ┃ # ┃
 ┣━━━┫  ┣━━━┫  ┣━━━┫  ┣━━━┫  ┣━━━┫     ┣━━━┫
 ┃ 1 ┃  ┃ 2 ┃  ┃ 3 ┃  ┃ 4 ┃  ┃ 5 ┃     ┃ # ┃
 ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛     ┗━━━┛
"""

t = format
for i in range(1,6):
  t = t.replace(str(i),"✘")
print(t)

def calcdisp(y, z, b):
  x = format
  if y == z:
    x = x.replace("#","✔",b)
  else:
    x = x.replace("#","✘",b)
  
  for a in range(0,5):
    if y[a] == z[a]:
      x = x.replace(str(a+1),"✔")
    else:
      if y[a] in z:
        x = x.replace(str(a+1),"!")
      else:
        x = x.replace(str(a+1),"✘")
  for a in range(0,5):
    x = x.replace("?",y[a],1)
  print(x)

ar = json.load(open("data.json", 'r'))
target = r.choice(ar)
#print(target) 
#the above is just used for testing so that you can see the random word chosen

guessed = False
count = 0
while guessed == False:
  user_guess = input("┃ Guess: ")
  os.system("clear")
  calcdisp(user_guess,target,count+1)
  count += 1
  if count >= 5 :
    print("""┏━━━━━━━━━━┓
┃ YOU LOST ┃
┗━━━━━━━━━━┛""")
    break
  if user_guess == target:
    print("""┏━━━━━━━━━┓
┃ YOU WON ┃
┗━━━━━━━━━┛""")
    break
