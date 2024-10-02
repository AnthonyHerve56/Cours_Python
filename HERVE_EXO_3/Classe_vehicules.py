from abc import ABCMeta, abstractmethod
 
""" You can use classes below or create your own 👍️"""
 
class UnmannedVehicule(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    __field=None
    def __init__(self,field="Spatio-Temporel"):
        self.__field=field
    
    @abstractmethod
    def Mission(self):
        print("Redéfinis-moi connard !")
        
    # getter
    @property
    def field(self):
        return self.__field
 
class AerialVehicule(metaclass=ABCMeta):
    """ A vehicle made for aerial areas."""
    def __init__(self,nombres_ailes=0,):
        
        self.__nombres_ailes=nombres_ailes
        
    @property
    def nombres_ailes(self):
        return self.__nombres_ailes
    
    
    
    
class GroundVehicule(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    pass
class UnderseaVehicule(metaclass=ABCMeta):
    """ A vehicle made for underwater sea."""
    pass
 
class UAV(UnmannedVehicule,AerialVehicule):
    """Unmanned Aerial Vehicule"""
    def __init__(self,nombres_ailes=4):
        
        UnmannedVehicule.__init__(self,"Air")
        AerialVehicule.__init__(self,nombres_ailes)
    
    def Mission(self):
        print("I believe i can fly ! I believe i can touch the sky")
class UUV(UnmannedVehicule,GroundVehicule):
    """Unmanned Undersea Vehicule"""
    def __init__(self):
        
        UnmannedVehicule.__init__(self,"Water")
    
    def Mission(self):
        print("Please help i'm under the water")
        
    	

class UGV(UnmannedVehicule,GroundVehicule):
    """Unmanned Ground Vehicule"""
    def __init__(self):
        
        UnmannedVehicule.__init__(self,"Ground")
        
    
    def Mission(self):
        print("15 kilomètres à pieds ça use ça use ! 15 killomètres à pieds ça use les chenilles")