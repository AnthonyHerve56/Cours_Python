import time

class Robot:
    
    __power = False
    __current_speed = 0
    __states = ['shutown', 'running']
    
    def __init__(self,battery_level=0):
        
        self.battery_level = battery_level
        
    def allumer_robot(self):
        # Allume le robot, on passe son power
        print("On allume le robot")
        self.__power=True
    
    def eteindre_robot(self):
        print("On éteint le robot")
        self.__power=False
    
    def recharger_robot(self,target_battery):
            # On vérifie que la charge de batterie voulu sois inférieur à celle actuelle
        if target_battery > self.__battery_level:
            # Si batterie souhaité supérieur à 100 on le remet à 100
            if(target_battery>100):
                target_battery=100
            pas=10
            #On calcul la dizaine et unité à recharger 
            #La dizaine servira pour le nombre de fois où on va ajouter 10
            dizaine=int(((target_battery-self.battery_level)/10)%10)
            unite=(target_battery%10)-(self.battery_level%10)
            i=0
            while i<dizaine:
                #On boucle et on ajoute +10% de batterie toutes les secondes tant que i < dizaine. C'est à dire tant qu'on a pas atteint la dizaine
                #de la valeur souhaité
                self.battery_level+=pas
                time.sleep(1)
                i+=1
                print(f"La charge de la batterie est de {self.battery_level}%")
            #Puis si il reste des unités on l'ajoute à la batterie restante
            time.sleep(unite/10)
            self.battery_level+=unite
            print(f"La charge de la batterie est de{self.battery_level}%")
        else:
            print("Batterie souhaité plus basse que batterie actuelle")
    
    def __str__(self): # must return a string
        if(self.__power==True):
            return f"Le robot est allumé, sa batterie restante est de {self.battery_level}% et il se déplace à une vitesse de {self.__current_speed}m/s"
        else:
            return f"Le robot est éteint, sa batterie restante est de {self.battery_level}%"
            
        
    def set_vitesse_de_deplacement(self,vitesse):
        self.__current_speed=vitesse
        
    def get_vitesse_de_deplacement(self):
        return self.__current_speed
    
    def arreter_robot(self):
        print("On arrete le robot")
        self.__current_speed=0
        
    
    