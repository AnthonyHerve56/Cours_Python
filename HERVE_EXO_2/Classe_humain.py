class Humain:
    # Nombre d'aliments mangés
    __manger=0 
    # Liste de tous les aliments mangés
    __aliments_manges=[]
    def __init__(self,genre,name="undefined"):
        self.name=name
        self.genre = genre
    
    def manger_Aliment(self,aliment):
        self.__manger+=1
        self.__aliments_manges.append(aliment)
        
    def digerer_aliments(self):
        print("Il semble que je dois afk bio")
        self.__aliments_manges.clear()
        
    
        