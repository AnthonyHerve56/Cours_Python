import Classe_Plateau
from Classe_Robot import Robot
import random

longueur=5
largeur=5
i=0
j=[]
Plateau=Classe_Plateau.Plateau(longueur,largeur)
Robot=Robot(0,0)


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
    if Robot.x >longueur or Robot.y>largeur:
        
        j.append(i)
        #print(f"J'ai fini une boucle {j}")
        i=0
        Robot.Reinitialise_position()
        if len(j)>1000:
            break


#print(f"On a fait ces nombre de mouvements {j}")
print(f"La moyenne du nombre de sortie est de {sum(j) / len(j)} mouvement")