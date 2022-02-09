import random

def gamewin(comp,you):
  if comp == you:
      return None
    elif comp =='s':
          if you=='w'
            return False
        elif you =='g':
            return True
    elif comp =='w':
          if you =='g':
            return False
        elif you =='s':
            return True      
    elif comp =='g':
          if you =='s':
               return False
        elif you =='w':
           return True
                   
print("comp turn:snake(s) water(w) or gun(g)")
randNo ==1:
   comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
 you = input("your turn: snake(s) water(w) or gun(g)?")
 a = gamewin(comp,you)

 print(f"computer chose {comp}")
 print(f"you chose {you}")

 if a == None:
     print("the game is a tie!")
     elif a: 
         print("you won!")
     else:
        print ("you lose!")   

      