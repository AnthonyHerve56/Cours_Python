import Classe_Plateau
import Classe_Robot
import random
import numpy as np
longueur=5
largeur=5

i=0
j=[]
Plateau=Classe_Plateau.Plateau(longueur,largeur)
Robot=Classe_Robot.Robot(0,0)


while True:
    deplacement=random.randint(1,4)
    if deplacement==1:
        Robot.Aller_a_droite()
    elif deplacement==2:
        Robot.Aller_a_gauche()
    elif(deplacement==3):
        Robot.Monter()
    else:
        Robot.Descendre()
    i+=1
    if Robot.x >longueur-1 or Robot.y>largeur-1:

        break
    A = np.zeros((longueur,largeur))
    A[Robot.x,Robot.y]=4
    print(f"{A}\n")

    
print(f"On a réussi en {i} nombre d'essai")