import os, random as r, json

format = """            ┏━━━━━━━━┓
            ┃ WORDLE ┃
            ┗━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
┃ ✘ = Incorrect Letter & Placement ┃   
┃ ! = Correct Letter & Wrong Place ┃   ┏━━━┳━━━┓ 
┃ ✔ = Correct Letter & Placement   ┃   ┃ # ┃ # ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   ┣━━━╋━━━┫  ┏━━━━━━━┓
                                       ┃ # ┃ # ┃  ┃ TRIES ┃
 ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓  ┏━━━┓     ┣━━━╋━━━┫  ┗━━━━━━━┛
 ┃ ? ┃  ┃ ? ┃  ┃ ? ┃  ┃ ? ┃  ┃ ? ┃     ┃ # ┃ # ┃
 ┣━━━┫  ┣━━━┫  ┣━━━┫  ┣━━━┫  ┣━━━┫     ┗━━━┻━━━┛
 ┃ 1 ┃  ┃ 2 ┃  ┃ 3 ┃  ┃ 4 ┃  ┃ 5 ┃
 ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛  ┗━━━┛     
"""

# Sets the first display to have crosses in place of numbers so that display format is same across all rounds.
fTF = format
for i in range(1,6):
  fTF = fTF.replace(str(i),"✘")
print(fTF)

# Function that runs through the display format and calculates each part of the user's input that lines up with the correct guess etc. while replacing the placeholder values in the display format to be displayed.
def calcdisp(userGuess, correctGuess, b):
  display = format
  if userGuess == correctGuess:
    display = display.replace("#","✘",b-1)
    display = display.replace("#","✔",1)
  else:
    display = display.replace("#","✘",b)
  for iter in range(0,5):
    if userGuess[iter] == correctGuess[iter]:
      display = display.replace(str(iter+1),"✔")
    else:
      if userGuess[iter] in correctGuess:
        display = display.replace(str(iter+1),"!")
      else:
        display = display.replace(str(iter+1),"✘")
  for iter in range(0,5):
    display = display.replace("?",userGuess[iter],1)
  print(display)

words = json.load(open("data.json", 'r'))
toGuess = r.choice(words)
#print(toGuess) 
#the above is just used for testing so that you can see the random word chosen

guessed = False
count = 0
while guessed == False:
  user_guess = input("┃ Guess: ")
  if user_guess in words:
    os.system("clear")
    calcdisp(user_guess,toGuess,count+1)
    count += 1
    if count >= 6 :
      print("""       ┏━━━━━━━━━━┓ ┏━━━━━━━┓
       ┃ YOU LOST ┃ ┃ """ + str(toGuess) + """ ┃
       ┗━━━━━━━━━━┛ ┗━━━━━━━┛""")
      break
    if user_guess == toGuess:
      print("""            ┏━━━━━━━━━┓
            ┃ YOU WON ┃
            ┗━━━━━━━━━┛""")
      break
