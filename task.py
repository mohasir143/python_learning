# random puzzle task            - Generate a random value with predefined data and 
# get input from user if it matches throw message as you guessed correctly , 
# if it is wrong have to guess until correct. if guessed correctly ask do you want to play again , 
# if yes means continue a game. no means exit from game.


while True:
 print("--------------------------------------------------")
 print(["one","two","three","four","five"])
 guess=input("choose the word in above sentence:")

 mylist=["one","two","three","four","five"]

 import random

 rannum=random.choice(mylist)
 print(rannum)


 if rannum==guess:
   print("congratulation...........you win the game!.")
   play_again=input("Do you want to play again: yes / no")
   if play_again=="yes":
      guess=input("choose the word in above sentence:")
   else:
     break
     
 else:
    print("you lose the game............try better next game!")
    guess=input("choose the word in above sentence:")



#                                                                       SUM=0
