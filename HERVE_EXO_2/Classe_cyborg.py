from Classe_Robot import Robot
from Classe_humain import Humain


class Cyborg(Robot,Humain):
    def __init__(self,genre,name="undefined",battery="0"):
        print(name,battery)
        Robot.__init__(self,battery)
        Humain.__init__(self,genre,name)
        
    def afficher_cyborg(self):
        print(f"Je suis un cyborg. Je m'appele {self.name}, je suis un {self.genre} et j'ai {self.battery_level}% de batterie")
        
    def Bruler_des_choses(self):
        print("BIIIIIIILIIIIIIYEEEEEEE il est l'heure de cramer des trucs")
        
    def __str__(self): # must return a string
        return f"Je suis un cyborg. Je m'appele {self.name}, je suis un {self.genre} et j'ai {self.battery_level}% de batterie"
