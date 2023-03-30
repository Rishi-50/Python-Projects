import random

def game(comp,you):
    if(comp == you):
        return None
    elif(comp=='w'):
        if(you=='s'):
            return False
        if(you=='g'):
            return True

    elif(comp=='s'):
        if(you=='w'):
            return False
        if(you=='g'):
            return True

    elif(comp=='g'):
        if(you=='w'):
            return False
        if(you=='s'):
            return True       

print("Computer turn: Snake(s) Water(w) Gun(g)?")
rand=random.randint(1,3)
if rand == 1:
    comp ='s'
elif rand == 2:
    comp ='w'
elif rand == 3:
    comp ='g'
  
you = (input("Player's turn: Snake(s) Water(w) Gun(g)?"))
  
win = game(comp ,you)

print(f"Computer chose:{comp}")
print(f"You chose:{you}")

if win==None:
    print("The game is a tie!")
elif win:
    print("You Win the game!")
else:
    print("You Lose the game!")