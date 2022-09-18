# BONUS - jeu plus petite / plus grande with  cheating detection
import random

Poss = [0, 101] # This array will hold the smallest and biggest integers that still can be guessed
                         # We initialize with the intervals

print("Mémorisez un nombre entre 1 et 100, je vais essayer de le retrouver. Et ne trichez pas ensuite")

def Guess(Poss, turn):

    if Poss[1] < Poss[0] or Poss[1] == Poss[0] or Poss[0] + 1 == Poss[1]:
        print("Tricheur !!!! \nVous avez dit plus grande que ", Poss[0], "mais aussi plus petite que ", Poss[1],"\nJ'ai gangé par forfait en ", turn, "coups !!!")
        return
    
    if Poss[0] + 2 == Poss[1]:
        guess = int((Poss[0] + Poss[1])/2)
    else:
        guess = random.randrange(Poss[0] + 1, Poss[1] - 1)

    turn += 1
    print("Je propose ", guess, "... +, - ou G ?") 
    entree = str(input())
    
    if entree == "G":
        print("J'ai trouvé ", guess, "en ", turn,"coups !!!")
        return   
    elif entree == "-":
        Poss[1] = guess
        Guess(Poss, turn)
    elif entree == "+":
        Poss[0] = guess
        Guess(Poss, turn)
        
    else:
        print("Input invalide, on recommence")
        Guess(Poss, turn)

Guess(Poss, turn = 0)