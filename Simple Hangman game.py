import random

def graphics(guess,word):
    if guess == 7:
        print('-----------')
        print('            ')
        print('     0     ')

    elif guess == 6:
        
        print('-----------')
        print('            ')
        print('     0     ')
        print('     |     ')
       
    elif guess==5 :
        print('-----------')
        print('            ')
        print('     0     ')
        print('     |     ')
        print('     |     ')
        
    elif guess == 4:
        print('-----------')
        print('            ')
        print('      0     ')
        print('     \|     ')
        print('      |     ')
        
        
    elif guess == 3:
        print('-----------')
        print('            ')
        print('      0     ')
        print('     \|/    ')
        print('      |     ')
    elif guess == 2:
        print('-----------')
        print('            ')
        print('      0     ')
        print('     \|/     ')
        print('      |     ')
        print('     /|     ')
    elif guess == 1:
        print('-----------')
        print('            ')
        print('      0     ')
        print('     \|/     ')
        print('      |     ')
        print('     /|\     ')
    else :
        print('-----------')
        print('          |  ')
        print('          |   ')
        print('      0 --     ')
        print('     /|\   ')
        print('      |     ')
        print('     /|\     ')
        print("GAME OVER!!!!!!")
        print("The word was",word)
        

        
word_set=['apple','guava','mosambi','watermelon','orange','pineapple','jackfruit',
          'lemon','chickoo','kiwi','passionfruit','cherry','gooseberry','strawberry',
          'blackberry']
word= random.choice(word_set)
length=len(list(word))
name=input("Welcome to hangman... Please enter your name to play")
print("Welcome ",name,"!!!!... Lets play Hangman")
print("Rules".center(50))
print("-----".center(50))
print("  #You have to guess the letters of a given word and Save the man from death")
print("  # U can guess one alphabet at a time.. and there are 8 guesses provided for you")
print("  if ur guess is crct then the spaces will be filled where the letter belong in the word")
print("  ")
response=0
guess=8
answer=[]
print(" It is a fruit with",length,"number of letters")
for i in range(length):# printing the word in blanks
    answer.append('-')
    
    filledletters= random.sample(word,2)
for letter in filledletters:
    n=word.index(letter) # Filling random letters for player
    answer.pop(n)
    answer.insert(n,letter)
print(answer)
while guess >= 1:
   print("Guess a letter...U have",guess,"guesses remaining")
   userr=input()
   response+=1
   if userr in word:
      if word.count(userr) > 1:
           n=word.index(userr)
           answer.pop(n)
           answer.insert(n,userr)
           n1=word.index(userr,n+1)
           answer.pop(n1)
           answer.insert(n1,userr)
      else:
           n=word.index(userr)
           answer.pop(n)
           answer.insert(n,userr)
          
           # Fixed problem for repeated letter words
      
      print("HOLAA!!")
      print(answer)
   else:
       print("Wrong guess")
       guess-=1
       graphics(guess,word)# Writ the hangman function
       print('strikee')#Removethiss
   if '-' not in answer:
       print('You Won!!!')
       break
        
        


        



          
        
