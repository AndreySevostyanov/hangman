import fileinput
import os
import random

from IPython import display

def getword(): 
  rndword = '' 
  x = os.scandir(path='/content/drive/MyDrive/game')
  paths = []
  for i in x:
    if i.is_file and i.name.endswith('.txt'):
      paths.append(i.path)

  with fileinput.input(files=(paths)) as f:
    for line in f:
      rndword=random.choice(list(f))
  return rndword.strip()

tolosecounter=0

def game():
  usedletters=[]
  guessedletters=[]
  wrongletters=[]
  rightword=[]
  
  global tolosecounter
  win=True
  rndword = getword()
  for w in rndword:
    rightword.append(w)
  print(rightword)
  print('The word contains ',len(rndword),' letters')
  while win:
    man()
    print('Used letters ',usedletters)
    print('Guessed letters ',guessedletters)
    print('Wrong letters', wrongletters)
    print(str(guessedletters))
    a=set(guessedletters)
    b=set(rightword)
    if a==b:
      print('You won the word was ',rndword,', congrats')
      win=False
    elif guessedletters!=rightword:
      # print('You won the word was ',rndword,' congrats')
      if tolosecounter<6:
        playerletter = input('Input a letter ')
        playerletter=playerletter.lower
        display.clear_output()
        
        if len(playerletter)>1:
          print('U\'ve inputed more than one letter')
          continue
        elif playerletter in rndword:
          if playerletter in usedletters:
            print('letter is already used, try another')
            continue
          else:
            if playerletter in rndword:
              usedletters.append(playerletter)
              guessedletters.append(playerletter)
        elif playerletter not in rndword:
          usedletters.append(playerletter)
          wrongletters.append(playerletter)
          tolosecounter+=1
      else:
        win=False
        print('You lose, the right word is ' + rndword)
def man():
  global tolosecounter
  global rndword
  if tolosecounter==0:
    print('______')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
  elif tolosecounter==1:
    print('______')
    print('|    |  ')
    print('|    0')
    print('|')
    print('|')
    print('|')
  elif tolosecounter==2:
    print('______')
    print('|    |  ')
    print('|    0')
    print('|    |  ')
    print('|')
    print('|')
  elif tolosecounter==3:
    print('______')
    print('|    |  ')
    print('|    0')
    print('|   /|  ')
    print('|')
    print('|')
  elif tolosecounter==4:
    print('______')
    print('|    |  ')
    print('|    0')
    print('|   /|\  ')
    print('|')
    print('|') 
  elif tolosecounter==5:
    print('______')
    print('|    |  ')
    print('|    0')
    print('|   /|\  ')
    print('|   /')
    print('|')
  elif tolosecounter==6:
    print('______')
    print('|    |  ')
    print('|    0')
    print('|   /|\  ')
    print('|   / \ ')
    print('|')
game()
